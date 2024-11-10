# from __future__ import print_function
import africastalking
from django.conf import settings

username = settings.USER
api_key = settings.API_KEY



def format_phone_number(phone_number):
    # Extract the first number if phone_number is a list
    if isinstance(phone_number, list):
        phone_number = phone_number[0]

    # Check if the phone number is already in the correct format: +2547XXXXXXXX
    if phone_number.startswith('+254') and len(phone_number) == 13 and phone_number[4:].isdigit():
        return phone_number

    # Check if the phone number starts with 07 and has 10 digits (e.g., 0712345678)
    elif phone_number.startswith('07') and len(phone_number) == 10 and phone_number[1:].isdigit():
        return '+254' + phone_number[1:]  # Convert 0712345678 to +254712345678
    
    elif phone_number.startswith('01') and len(phone_number) == 10 and phone_number[1:].isdigit():
        return '+254' + phone_number[1:]  # Convert 0112345678 to +254712345678

    # Invalid format; inform the user
    else:
        raise ValueError("Invalid phone number format. Please provide a valid Kenyan phone number in the format +2547XXXXXXXX or 07XXXXXXXX.")


def send_message(send_to, order_number, customer_name):
    
    try:
        formatted_phone_number = format_phone_number(send_to)
    except ValueError as e:
        print(f"Errorasdas: {e}")
        return
    
    print('recipients', formatted_phone_number)
    africastalking.initialize(username, api_key)
    # # Get the SMS service
    sms = africastalking.SMS
    
    # recipients = ["+254728265330"]
    recipients = ["+254799740253", "+254113450333"]
    # recipients = [formatted_phone_number]
    # # Set your message
    # # message = "I'm a lumberjack and it's ok, I sleep all night and I work all day"
    message = f"Dear {customer_name}, Thank you for making your order from BARAKA GAS POINT. Wea are processing Your order number is [{order_number}]. All orders require payments before delivery. You can call us on 0701593906"
    # # Set your shortCode or senderId
        
    # sender = "baraka gas point"
    try:
    #     # Thats it, hit send and we'll take care of the rest.
        response = sms.send(message, recipients)
        print (response)
    except Exception as e:
            print ('Encountered an error while sending: %s' % str(e))




# class SMS:
#     def __init__(self):
#         # Set your app credentials

        
            
#         self.username = settings.username
#         self.api_key = settings.api_key
        
        
#         # Initialize the SDK
#         africastalking.initialize(self.username, self.api_key)
        
#         # Get the SMS service
#         self.sms = africastalking.SMS
         
#     def send(self):
#         # Set the numbers you want to send to in international format
#         recipients = ["+254713YYYZZZ", "+254733YYYZZZ"]
#         # Set your message
#         message = "I'm a lumberjack and it's ok, I sleep all night and I work all day"
        
#         # Set your shortCode or senderId
            
#         sender = "shortCode or senderId"
#         try:
#             # Thats it, hit send and we'll take care of the rest.
#             response = self.sms.send(message, recipients, sender)
#             print (response)
#         except Exception as e:
#                 print ('Encountered an error while sending: %s' % str(e))

# if __name__ == '__main__':
#     SMS().send()