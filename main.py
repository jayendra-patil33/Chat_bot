# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 00:50:08 2019
changed a comment
@author: JAY
"""


import json
import os
from pyowm import OWM
import json_create

from flask import Flask
from flask import request
from flask import make_response

import requests

API_ENDPOINT_RICE= "https://api.data.gov.in/resource/0c05e610-698d-4930-8166-a0893c2d9862?api-key=579b464db66ec23bdd00000121814e6c9881416652f58fd832b30b08&format=json&offset=0&limit=10000"
API_ENDPOINT_CORRIANDER= "https://api.data.gov.in/resource/56efc412-c026-4640-b106-d4a7f615b025?api-key=579b464db66ec23bdd00000121814e6c9881416652f58fd832b30b08&format=json&offset=0&limit=20000"
API_ENDPOINT_GREEN_CHILLI = "https://api.data.gov.in/resource/b0f998ff-315e-42ee-b980-0d3af00fb1bc?api-key=579b464db66ec23bdd00000121814e6c9881416652f58fd832b30b08&format=json&offset=0&limit=25000"

# Flask app should start in global layout
app = Flask(__name__)
            
@app.route('/', methods=['GET'])
def hello_world():
    return("helloworld")
    
@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    #print("Request:")
    #print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    global rice, corriander,green_chilli
    if req.get("queryResult").get("action") == "price_rice":
        
        result = req.get("queryResult")
        parameters = result.get("parameters")
        zone = parameters.get("state")
        district=parameters.get("district")
        b=[]
        for x in rice:
            if(x['district']==district):
                # print(x)
                b.append(x)
        if(len(b)==0):
            return {
                    "fulfillmentText":"No price to show :(",
                    "source": "price_rice"
                }
        else: 
            minima=b[0]     
            for x in b:
                if(x['modal_price']<=minima['modal_price']):
                    minima=x
            print(minima)    
            speec= "The price of rice in " +minima['state']+','+minima['district']+" in "+minima['market']+' market'+' of variety '+minima['variety'] + " is " + str(minima['modal_price'])
            print("Response:")
            print(speec)
            return {
                    "fulfillmentText": speec,
                    "source": "price_rice"
                }
    elif req.get("queryResult").get("action") == "price_corriander":
        result = req.get("queryResult")
        parameters = result.get("parameters")
        zone = parameters.get("state")
        district=parameters.get("district")
        corr=[]
        for x in corriander:
            if(x['district']==district):
                # print(x)
                corr.append(x)
        minima=corr[0]     
        for x in corr:
            if(x['modal_price']<=minima['modal_price']):
                minima=x
        print(minima)    
        speec= "The price of corriander in " +minima['state']+','+minima['district']+" in "+minima['market']+' market'+' of variety '+minima['variety'] + " is " + str(minima['modal_price'])
        print("Response:")
        print(speec)
        return {
                "fulfillmentText": speec,
                "source": "price_rice"
              }
    elif req.get("queryResult").get("action") == "price_green_chilli":
        result = req.get("queryResult")
        parameters = result.get("parameters")
        zone = parameters.get("state")
        district=parameters.get("district")
        green=[]
        for x in green_chilli:
            if(x['district']==district):
                # print(x)
                green.append(x)
        minima=green[0]     
        for x in green:
            if(x['modal_price']<=minima['modal_price']):
                minima=x
        print(minima)    
        speec= "The price of green chilli in " +minima['state']+','+minima['district']+" in "+minima['market']+' market'+' of variety '+minima['variety'] + " is " + str(minima['modal_price'])
        print("Response:")
        print(speec)
        return {
                "fulfillmentText": speec,
                "source": "price_rice"
              }
    else:
        result = req.get("queryResult")
        parameters = result.get("parameters")
        zone = parameters.get("city")
        
        OWMKEY = '1ff3ea822ff4cf6a648a61564c5992f4'
        owm = OWM(OWMKEY)
        strin=str(zone)+","+"IN"
        obs = owm.weather_at_place(strin) 
        w = obs.get_weather() #
        l = obs.get_location()
        status = str(w.get_detailed_status()) 
        placename = str(l.get_name()) 
        wtime = str(w.get_reference_time(timeformat='iso')) 
        temperature = str(w.get_temperature('celsius').get('temp'))
        print(status,placename,wtime,temperature)
        speech ="Weather at "+zone+": "+status+", "+temperature+" C, "+wtime
        print("Response:")
        print(speech)
        return {
                "fulfillmentText": speech,
                #"displayText": speech,
                #"data": {},
                #"contextOut": [],
                "source": "price_rice"
              }        
              
rice=json_create.json_create(API_ENDPOINT_RICE)
corriander=json_create.json_create(API_ENDPOINT_CORRIANDER)
green_chilli=json_create.json_create(API_ENDPOINT_GREEN_CHILLI)

if __name__ == '__main__':
    
    port = int(os.getenv('PORT', 80))
    
    print ("Starting app on port %d" %(port))

    app.run(debug=True, port=port, host='0.0.0.0')
