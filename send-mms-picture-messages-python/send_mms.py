# we import the Twilio client from the dependency we just installed
from twilio.rest import Client

# the following line needs your Twilio Account SID and Auth Token
client = Client("ACxxxxxxxxxxxxxx", "zzzzzzzzzzzzz")

# this is the URL to an image file we're going to send in the MMS
media = "https://raw.githubusercontent.com/mattmakai/fullstackpython.com/master/static/img/logos/f.png"

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send MMS to any phone number that MMS is available
client.messages.create(to="+19732644152",
                       from_="+12023351278",
                       body="MMS via Python? Nice!",
                       media_url=media)

