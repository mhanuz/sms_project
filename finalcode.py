from datetime import datetime
from twilio.rest import Client
import time



# Data in dictionary format 
user_info = {"name": 
    [
    {'hashem':{'Time':["12:03:01","15:07:04","08:05:03"]}}, 
    {'kashem':{'Time':["11:04:05","14:06:03","09:04:09"]}},
    {'abul':{'Time':["14:09:08","16:08:06","18:07:09"]}},
    ] 
    }

# print(user_info['name'])

# Update time in every second for checking

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

# assign twilio client
client = Client('AC58116279b81f5fa202edadc3eed8e15a', "5a82a3c9abe73b342e31a979f852eba3")

while (True):

    # find out user name and make a list 
    name_key=[]
    for name in user_info['name']:
        for key in name.keys():
            name_key.append(key)

    # filtering our raw data 
    time_data=[]
    for i,data in enumerate(user_info['name']):
        time_data=data[name_key[i]]['Time']
        for singleTime in time_data:
            # current_user_name = name_key[i]
            # print(singleTime,name_key[i])
            time_split = singleTime.split(':')
            sms_hour = time_split[0]
            sms_min = time_split[1]
            sms_sec =time_split[2]

            new_hour=Update_Hour()
            new_min=Update_Min()
            new_sec=Update_Sec()

            print(new_hour,new_min,new_sec)
            if ((new_hour==sms_hour) and (new_min==sms_min) and(new_sec==sms_sec)):
                print("Time Matched")
                client.messages.create(
                    body=f'Hi,{name_key[i]}, Greetings from our site.... have a nice day',
                    from_='+19376331061',
                    to='+8801957060587'
                )
                time.sleep(2) # keep watting everything for 2 seconds 




