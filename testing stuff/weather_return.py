# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 00:50:08 2019

@author: JAY
"""


import json
import os
from pyowm import OWM

from flask import Flask
from flask import request
from flask import make_response

import requests

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/hey', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("queryResult").get("action") == "price":
        
        '''result = req.get("queryResult")
        parameters = result.get("parameters")
        zone = parameters.get("state")
        district=parameters.get("district")

        
        API_ENDPOINT = "https://api.data.gov.in/resource/0c05e610-698d-4930-8166-a0893c2d9862?api-key=579b464db66ec23bdd00000121814e6c9881416652f58fd832b30b08&format=json&offset=0&limit=10000"
  
        
        #header = {'content-type': 'application/json','accept': 'application/json'} 
        # data to be sent to api 
        #data1 = {'format':'Json','offset':1,'limit':1,} 
  
        # sending post request and saving response as response object 
        r = requests.get(url = API_ENDPOINT)#, data = data1,headers=header) 
        a=r.json()
        
        b=[]
        for x in a["records"]:
            if(x['state']==zone and x['district']==district):
                print(x)
                b.append(x)
        minima=b[0]     
        for x in b:
            if(x['modal_price']<=minima['modal_price']):
                minima=x
        print(minima)    '''

        #speec= "The price of rice in " +minima['state']+','+minima['district']+" in "+minima['market']+' market'+' of variety '+minima['variety'] + " is " + str(minima['modal_price'])
        speec="hi there"
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
        obs = owm.weather_at_place(zone+","+"IN") 
        w = obs.get_weather() 
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
                "source": "weather"
              }        
if __name__ == '__main__':
    #port = int(os.getenv('PORT', 80))

    print("Starting app on port %d" %(port))

    app.run(debug=True, port=80, host='0.0.0.0')
