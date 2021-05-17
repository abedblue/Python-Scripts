import requests
import time
from urllib.parse import urlencode

url = 'http://h2ogo.app/scan-api'
pingurl = 'http://h2ogo.app/ping-api'
device = '123'
minutes = 0
header = {"content-type": "text/html"}

while True:
    if minutes % 10 == 0:
        try:
            myping = {'secret_key': 'supersecret', 'device_id': str(device)}
            z = requests.post(pingurl, data = myping)
            print(z.text)
        except:
            print("ping err")
            print(z.text)
    minutes += 1
    #print("start1")
    #print(minutes)
    if minutes % 2 == 1:
        try:
            toWrite = ""
            work1 = open("Work1.txt", "r+")
            for x in work1:
                if len(x) > 0:
                    try:
                        token = x[0:x.index(" ", 0)]
                        now = x[x.index(" ", 0)+1:x.index(" ", x.index(" ", 0)+1)]
                        myobj = {'token_id': str(token), 'date_scanned': now, 'secret_key': 'supersecret', 'device_id': device}
                        y = requests.post(url, data = myobj)                      
                        if str(y.text) != "1":
                            toWrite += x
                            print("API error code:")
                            print(y.text)
                    except:
                        print("err")
                        toWrite += x
            work1.seek(0)
            work1.truncate(0)
            work1.write(toWrite)
            work1.close()
            #print(toWrite)
        except:
            print("err")
    #print("end1")
    time.sleep(30)
    minutes += 1
    #print("start2")
    #print(minutes)
    if minutes % 2 == 0:
        try:
            toWrite = ""
            work = open("Work2.txt", "r+")
            for x in work:
                if len(x) > 0:
                    try:
                        token = x[0:x.index(" ", 0)]
                        now = x[x.index(" ", 0)+1:x.index(" ", x.index(" ", 0)+1)]
                        myobj = {'token_id': str(token), 'date_scanned': now, 'secret_key': 'supersecret', 'device_id': device}
                        y = requests.post(url, data = myobj)
                        if str(y.text) != "1":
                            toWrite += x
                            print("API error code:")
                            print(y.text)
                    except:
                        print("err")
                        toWrite += x
            work.seek(0)
            work.truncate(0)
            work.write(toWrite)
            work.close()
            #print(toWrite)
        except:
            print("err")            
    #print("end2")
    time.sleep(30)
