import smtplib
from twilio.rest import Client

TWILIO_SID = "a3f82k"
TWILIO_AUTH_TOKEN = "b3b9aecc213f479f878cdbcb3503bfd7"
TWILIO_VIRTUAL_NUMBER = "virtual phone number"
TWILIO_VERIFIED_NUMBER = "phone number"
MAIL_PROVIDER_SMTP_ADDRESS = 'SMTP ADDRESS "smtp.gmail.com"'
MY_EMAIL = "samrat1234@gmail.com"
MY_PASSWORD = "mypassword"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )