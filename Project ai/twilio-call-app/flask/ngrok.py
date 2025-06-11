from flask import Flask, Response
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/voice", methods=['GET', 'POST'])
def voice():
    response = VoiceResponse()
    response.say("Hello! This is a call from your Twilio bot.", voice='alice')
    return Response(str(response), mimetype='text/xml')

if __name__ == "__main__":
    app.run(debug=True)
