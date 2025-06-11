from flask import Flask, render_template, Response
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

# ✅ Twilio credentials
account_sid = 'AC00471ba98b14ffc21e3c86d4c1afb5bc'
auth_token = 'e7ed1246ece23f828837c55dc98d8a94'
twilio_number = '+12694484362'       # Your Twilio phone number
target_number = '+919949611408'      # Verified number to call

client = Client(account_sid, auth_token)

# 🔘 Home page route
@app.route('/')
def index():
    return render_template('index.html')

# 🔘 Call trigger route
@app.route('/call')
def call():
    try:
        call = client.calls.create(
            to=target_number,
            from_=twilio_number,
            url='https://your-ngrok-url.ngrok.io/voice'  # Replace this after running ngrok
        )
        return f'✅ Call initiated! Call SID: {call.sid}'
    except Exception as e:
        return f'❌ Call failed: {e}'

# 🔘 Voice TwiML response route
@app.route('/voice', methods=['POST'])
def voice():
    response = VoiceResponse()
    response.say("Hello! This is a test call from your AI assistant. Have a nice day!", voice='Polly.Joanna')
    return Response(str(response), mimetype='text/xml')

# 🔘 Run the app
if __name__ == '__main__':
    app.run(debug=True)
