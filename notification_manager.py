from twilio.rest import Client

TWILIO_SID = "AC65fdf3ce0cdc39934c9875bd68bb6406"
TWILIO_AUTH_TOKEN = "8108106e7321f7ba26fb68f06c273a5a"
TWILIO_VIRTUAL_NUMBER = "+19892624099"
TWILIO_VERIFIED_NUMBER = "+919398877936"


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
