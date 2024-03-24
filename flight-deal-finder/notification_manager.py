from twilio.rest import Client

TWILIO_SID = "a3f82k"
TWILIO_AUTH_TOKEN = "b3b9aecc213f479f878cdbcb3503bfd7"
TWILIO_VIRTUAL_NUMBER = "8389110907"
TWILIO_VERIFIED_NUMBER = "9773965964"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
