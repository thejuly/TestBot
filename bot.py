# -*- coding: utf-8 -*-
from flask import Flask, request
import json
import requests
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return "Hello World!"
#callback Webhook
@app.route('/callback', methods=['POST'])
def callback():
    json_line = request.get_json()
    json_line = json.dumps(json_line)
    decoded = json.loads(json_line)
    user = decoded["events"][0]['replyToken']
    #id=[d['replyToken'] for d in user][0]
    #print(json_line)
    print("User：",user)
    sendText(user,'Hellow') #Send Msg
    return '',200
 
def sendText(user, text):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    Authorization = '1sAimDh9L0wg5XAJeBYy96GrwzZFYQYAfTB+CrsdX5E/9gdt9oj5Lbc9NbRSHh5d05Ne9FDan12z6c9dbprv5TXRgjm4/+ioHTy6G91A2rNBiW999c0IlhsTcq5bfOyVf7OLRGtAAISIbHd84WemFgdB04t89/1O/w1cDnyilFU= ' #ENTER_ACCESS_TOKEN
 
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization':Authorization
    }
 
    data = json.dumps({
        "replyToken":user,
        "messages":[{
            "type":"text",
            "text":text
        }]
    })
 
    #print("Data：",data)
    r = requests.post(LINE_API, headers=headers, data=data) #Send Data
    #print(r.text)
 
if __name__ == '__main__':
     app.run(debug=True)
