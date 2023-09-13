import requests
import json


URL="http://127.0.0.1:8000/student_create/"

data={
    'name':'pankaj',
    'roll':20,
    'city':'lalitpur'
}

json_data=json.dumps(data)

r= requests.post(url=URL,data=json_data)

data=r.json()

print(data)

