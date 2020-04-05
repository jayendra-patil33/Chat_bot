def json_create(self,API_ENDPOINT)
 self.API_ENDPOINT =API_ENDPOINT 
    request = requests.get(url = self.API_ENDPOINT)
    request_json=request.json()
        
    relev=[]
    for x in a["records"]:
            if(x['state']=="Maharashtra" ):
                # print(x)
                b.append(x)