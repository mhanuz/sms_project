from twilio.rest import Client


# the following line needs your Twilio Account SID and Auth Token
client = Client('AC58116279b81f5fa202edadc3eed8e15a', "5a82a3c9abe73b342e31a979f852eba3")

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
client.messages.create(
    body='Hi, your test result is. Great job',
    from_='+19376331061',
    to='+8801957060587'
)