import vonage

client = vonage.Client(key="b631aadc", secret="9cqKKmLOeVU1AGks")
sms = vonage.Sms(client)


def senn():
    responseData = sms.send_message(
        {
            "from": "Vonage APIs",
            "to": "254110006669",
            "text": "A text message sent using the Nexmo SMS API",
        }
    )

    if responseData["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {responseData['messages'][0]['error-text']}")