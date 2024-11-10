from sinch import SinchClient
import os
from dotenv import load_dotenv

load_dotenv() 


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



sinch_client = SinchClient(
    key_id=os.getenv("access_key"),
    # key_id="YOUR_key_id",
    # key_secret="YOUR_key_secret",
    key_secret=os.getenv("key_secreat"),
    # project_id="YOUR_project_id"
    project_id=os.getenv("project_id")
)

send_batch_response = sinch_client.sms.batches.send(
    body="Hello from Sinch!",
    to=["254113450333"],
    from_="447418630487",
    delivery_report="none"
)

print(send_batch_response)