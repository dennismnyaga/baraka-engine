from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from.models import *
from .serializers import *
from .uwazii import send_sms, format_phone_number  # Ensure these are imported




# Create your views here.

class all_products(APIView):
    def get(self, request):
        products = Product.objects.all()
        serialize = ProductSerializers(products, many=True)

        return Response(serialize.data)
    

class single_product(APIView):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        serialize = ProductSerializers(product)

        return Response(serialize.data)
    

class related_product(APIView):
    def get(self, request, pk):
        product = Product.objects.filter()




class process_order(APIView):
    def get(self, request):
        order = Orders.objects.all()

    def post(self, request):
        try:
            print('data ', request.data)
            # Extract customer details and cart items from request data
            customer_data = request.data.get('customerDetails')
            cart_items = request.data.get('cartItems')

            if not customer_data or not cart_items:
                return Response({'error': 'Customer details and cart items are required.'}, status=status.HTTP_400_BAD_REQUEST)

            # Validate and create/retrieve the customer
            customer_serializer = CustomerSerializer(data=customer_data)
            if customer_serializer.is_valid():
                customer, created = Customer.objects.get_or_create(
                    phone=customer_data['phone'],
                    defaults={
                        'first_name': customer_data['first_name'],
                        'last_name': customer_data['last_name']
                    }
                )
            else:
                return Response(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            while True:
                order_number = random.randint(1000, 9999)
                if not Orders.objects.filter(order_number=order_number).exists():
                    break
            # Create an order for the customer
            order = Orders.objects.create(
                order_number=order_number,
                customer=customer,
                location=customer_data['location']
            )

            # Iterate over cart items and create OrderItem entries
            for item in cart_items:
                product = Product.objects.get(id=item['id'])
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=item['quantity']
                )

            
            
            # Send an SMS with the order number to the customer's phone number (example with Twilio)
            phone_number = customer_data['phone']
            send_to = phone_number
            # # send_to = ["+254" + int(phone_number)]

            customer_name = customer_data['first_name']
            location = customer_data['location']

            # response = send_message(numbers=number, message=message)

            try:
                phone_number = format_phone_number(customer_data['phone'])
                customer_name = customer_data['first_name']
                location = customer_data['location']

                # Construct the customer message
                customer_message = f"Hello {customer_name}, your order (#{order_number}) has been received and is being processed."

                # Construct the admin message
                admin_message = (f"New order received (#{order_number}) from {customer_name}. "
                                 f"Customer phone: {phone_number}, Location: {location}.")

                # Define the additional admin number
                additional_number = '+254701593906'  # Replace with the actual admin number as needed

                # Format the additional number
                formatted_additional_number = format_phone_number(additional_number)

                # Send SMS to the customer
                customer_sms_response = send_sms(numbers=[phone_number], message=customer_message)

                print('Customer d ', customer_sms_response)
                # Send SMS to the admin
                admin_sms_response = send_sms(numbers=[formatted_additional_number], message=admin_message)

                print('admin ', admin_sms_response)
                # Check if there were any errors in SMS sending
                if 'error' in customer_sms_response or 'error' in admin_sms_response:
                    return Response({'error': 'SMS could not be sent.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                
            except ValueError as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            # # selected_customer_with_debt_phone_numbers = ["+254" + str(customers_with_debts.phone) for customers_with_debts in customers_with_debts]
            # sms_message = f"Thank you for your order! Your order number is {order_number}."

            # send_batch_response()



            # Uncomment and configure this section to use Twilio or another SMS service
            # account_sid = 'your_account_sid'
            # auth_token = 'your_auth_token'
            # client = Client(account_sid, auth_token)
            # message = client.messages.create(
            #     body=sms_message,
            #     from_='+1234567890',  # Your Twilio number
            #     to=phone_number
            # )
            # print('SMS sent:', message.sid)
            
            # Serialize and return the created order
            order_serializer = OrderSerializer(order)
            return Response({'message': 'Order created successfully!', 'order': order_serializer.data}, status=status.HTTP_201_CREATED)

        except Product.DoesNotExist:
            return Response({'error': 'One or more products do not exist.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)