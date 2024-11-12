import requests
from datetime import datetime


API_URL = 'https://restapi.uwaziimobile.com/v1/send'

def format_phone_number(phone_number):
    """Formats the phone number to the required +254XXXXXXXXX format."""
    if isinstance(phone_number, list):
        phone_number = phone_number[0]

    if phone_number.startswith('+254') and len(phone_number) == 13 and phone_number[4:].isdigit():
        return phone_number
    elif phone_number.startswith('07') and len(phone_number) == 10 and phone_number[1:].isdigit():
        return '+254' + phone_number[1:]  # Convert 0712345678 to +254712345678
    elif phone_number.startswith('01') and len(phone_number) == 10 and phone_number[1:].isdigit():
        return '+254' + phone_number[1:]  # Convert 0112345678 to +254112345678
    else:
        raise ValueError("Invalid phone number format. Please provide a valid Kenyan phone number in the format +2547XXXXXXXX or 07XXXXXXXX.")

def send_sms(numbers, message, sender_id="SMS", sms_type="sms", lifetime=86400, delivery=False):
    """
    Sends an SMS using the provided API.
    
    Args:
    - numbers (list): List of phone numbers to send the message to.
    - message (str): The message content.
    - sender_id (str): The sender ID.
    - sms_type (str): The type of the SMS (default is 'sms').
    - lifetime (int): The message lifetime in seconds.
    - delivery (bool): Delivery receipt request.
    
    Returns:
    - dict: Response from the API.
    """
    headers = {
        'X-Access-Token': ACCESS_TOKEN,
        'Content-Type': 'application/json',
        'charset': 'UTF-8',
    }

    # Format all phone numbers before sending
    formatted_numbers = []
    for number in numbers:
        try:
            formatted_numbers.append(format_phone_number(number))
        except ValueError as e:
            return {'error': str(e)}

    payload = [{
        'number': formatted_numbers,
        'senderID': 'Uwazii',
        'text': message,
        'type': sms_type,
        'beginDate': datetime.now().strftime("%Y-%m-%d"),
        'beginTime': datetime.now().strftime("%H:%M:%S"),
        'lifetime': lifetime,
        'delivery': delivery,
    }]

    response = requests.post(API_URL, json=payload, headers=headers)
    return response.json()