import os
from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse
from twilio.rest import Client


app = Flask(__name__)

# pulls credentials from environment variables
client = Client()

BASE_URL = os.getenv("BASE_URL")
twiml_instructions_url = "{}/record".format(BASE_URL)
recording_callback_url = "{}/callback".format(BASE_URL)

twilio_phone_number = os.getenv("TWILIO_PHONE_NUMBER")


@app.route("/record", methods=["GET", "POST"])
def record():
    """Returns TwiML which prompts the caller to record a message"""
    # Start our TwiML response
    response = VoiceResponse()

    # Use <Say> to give the caller some instructions
    response.say('Ahoy! Call recording starts now.')

    # Use <Record> to record the caller's message
    response.record()

    # End the call with <Hangup>
    response.hangup()

    return str(response)


@app.route("/dial/<int:phone_number>")
def dial(phone_number):
    """Dials an outbound phone call to the number in the URL. Just
    as a heads up you will never want to leave a URL like this exposed
    without authentication and further phone number format verification.
    phone_number should be just the digits with the country code first,
    for example 14155559812."""
    call = client.calls.create(
            to='+{}'.format(phone_number),
            from_=twilio_phone_number,
            url=twiml_instructions_url,
    )
    print(call.sid)
    return "dialing +{}".format(phone_number)


@app.route("/get-recording-url/<call_sid>")
def get_recording_url(call_sid):
    recording_urls = ""
    call = client.calls.get(call_sid)
    for r in call.recordings.list():
        recording_urls="\n".join([recording_urls, r.uri])
    return str(recording_urls)
