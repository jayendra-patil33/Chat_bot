import json_create

API_ENDPOINT=  "https://api.data.gov.in/resource/56efc412-c026-4640-b106-d4a7f615b025?api-key=579b464db66ec23bdd00000121814e6c9881416652f58fd832b30b08&format=json&offset=0&limit=20000"
json1= json_create.json_create(API_ENDPOINT)
print(json1)
