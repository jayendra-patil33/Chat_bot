import requests
def json_create(API_ENDPOINT):
    request = requests.get(url = API_ENDPOINT)
    request_json=request.json()
        
    relev=[]
    for x in request_json["records"]:
            if(x['state']=="Maharashtra" ):
                # print(x)
                relev.append(x)
    return(relev)            