import requests
import datetime
import sys

url = 'http://campcanadensis.h2ogo.app/scan-api'
device = '123'
token = 'null'

def storeActiveData(myToken, myDateTime, err):
    try:
        work = open("Work1.txt", "a")
        work.write(myToken + " " + str(myDateTime) + " " + device + " " + err + "\n")
        work.close
    except:
        work = open("Work2.txt", "a")
        work.write(myToken + " " + str(myDateTime) + " " + device + " " + err + "\n")
        work.close

while True:
    try:
        token = 'null'
        token = sys.stdin.readline()
        token = token[0:-1]
        if token == 'h':
            break
        now = datetime.datetime.utcnow().timestamp()
        myobj = {'token_id': token, 'date_scanned': now, 'secret_key': 'supersecret', 'device_id': device}
        x = requests.post(url, data = myobj)
        sys.stdout.write(x.text)
        records = open("Records.txt", "a")
        records.write(token + " " + str(now) + " " + device + " " + str(x.text) + "\n")
        records.close()
        if (str(x.text) != '1' and str(x.text) != '05' and str(x.text) != '02'):
            storeActiveData(token, now, str(x.text))
    except:
        sys.stdout.write("err")
        if token != 'null':            
            records = open("Records.txt", "a")
            records.write(token + " " + str(datetime.datetime.utcnow().timestamp()) + " " + device + " " + "Request Error" + "\n")
            records.close()
            storeActiveData(token, datetime.datetime.utcnow().timestamp(), "Request Error")
