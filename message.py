from datetime import datetime
from twilio.rest import Client
import time
client = Client('AC58116279b81f5fa202edadc3eed8e15a', "5a82a3c9abe73b342e31a979f852eba3")
def Update_Hour():
    now = datetime.now()
    current_Hour = int(now.strftime("%H"))
    return current_Hour

def Update_Min():
    now = datetime.now()
    current_Min = int(now.strftime("%M"))
    current_Sec = int(now.strftime("%S"))
    return current_Min

def Update_Sec():
    now = datetime.now()
    current_Sec = int(now.strftime("%S"))
    return current_Sec

sms_hour = 17
sms_min =1
sms_sec =5

while (True):
    new_hour=Update_Hour()
    new_min=Update_Min()
    new_sec=Update_Sec()


    if ((new_hour==sms_hour) and (new_min==sms_min) and(new_sec==sms_sec)):
        print("Time Matched")
        client.messages.create(
            body='Hi, your test result is. Great job',
            from_='+19376331061',
            to='+8801957060587'
        )
        time.sleep(2)
    
            
            

