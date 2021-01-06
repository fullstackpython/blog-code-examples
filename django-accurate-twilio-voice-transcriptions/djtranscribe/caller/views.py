from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse


def dial(request, phone_number):
    """Dials an outbound phone call to the number in the URL. Just
    as a heads up you will never want to leave a URL like this exposed
    without authentication and further phone number format verification.
    phone_number should be just the digits with the country code first,
    for example 14155559812."""
    # pulls credentials from environment variables
    twilio_client = Client()
    call = twilio_client.calls.create(
            to='+{}'.format(phone_number),
            from_=settings.TWILIO_PHONE_NUMBER,
            url=settings.TWIML_INSTRUCTIONS_URL,
    )
    print(call.sid)
    return HttpResponse("dialing +{}. call SID is: {}".format(
                            phone_number, call.sid))


@csrf_exempt
def record_twiml(request):
    """Returns TwiML which prompts the caller to record a message"""
    # Start our TwiML response
    response = VoiceResponse()

    # Use <Say> to give the caller some instructions
    response.say('Ahoy! Call recording starts now.')

    # Use <Record> to record the caller's message
    response.record()

    # End the call with <Hangup>
    response.hangup()

    return HttpResponse(str(response), content_type='application/xml')


def get_recording_url(request, call_sid):
    # pulls credentials from environment variables
    twilio_client = Client()
    recording_urls = ""
    call = twilio_client.calls.get(call_sid)
    for r in call.recordings.list():
        recording_urls="\n".join([recording_urls, "".join(['https://api.twilio.com', r.uri])])
    return HttpResponse(str(recording_urls), 200)
