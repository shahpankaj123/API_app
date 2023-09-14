import requests
import json


URL="http://127.0.0.1:8000/student_api/"

def getdata():
  data={
    'id':1
   }
  json_data=json.dumps(data)
  r= requests.get(url=URL,data=json_data)
  data=r.json()
  print(data)

def createdata():
  data={
    'name':'ram',
    'roll':174,
    'city':'birgung'
   }
  json_data=json.dumps(data)
  r= requests.post(url=URL,data=json_data)
  data=r.json()
  print(data)
    
#getdata()
createdata()

def deletedata():
  data={
    'id':2
   }
  json_data=json.dumps(data)
  r= requests.delete(url=URL,data=json_data)
  data=r.json()
  print(data) 

#deletedata()

def updatedata():
  data={
    'id':4,
    'name':'sita', 
    'city':'saptari' 
   }
  json_data=json.dumps(data)
  r= requests.put(url=URL,data=json_data)
  data=r.json()
  print(data)
  
#updatedata()  
  