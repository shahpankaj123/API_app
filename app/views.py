from django.shortcuts import render
from django.http import HttpResponse
from .models import student
from .serializer import *
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from django.views.decorators.csrf import csrf_exempt



def studentdetail(request,cid):
    
    stu=student.objects.get(id=cid)
    serializer=studentserializer(stu)   
    json_data=JSONRenderer().render(serializer.data)  
    return HttpResponse(json_data, content_type='application/json')

def student_all(request):
    
    stu=student.objects.all()
    serializer=studentserializer(stu,many=True)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
# Create your views here.

@csrf_exempt
def student_create(request):
    if request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=studentserializer(data=pythondata)
        
        if serializer.is_valid():
            serializer.save()
            res={'msg':'created successfully'}
            
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')

@csrf_exempt
def student_api(request):
    if request.method=='GET':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id')
        stu=student.objects.get(id=id)
        serializer=studentserializer(stu)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type="application/json")
    
    if request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        
        serializer=studentserializer(data=python_data)
        
        if serializer.is_valid():
            serializer.save()
            res={'msg':'data created'}
            
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
    
    
    if request.method=='DELETE':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        
        id=python_data.get('id')
        stu=student.objects.get(id=id)
        stu.delete()
        
        res={'msg':'data deleted successfully'}
            
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method=='PUT':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id')
        stu=student.objects.get(id=id)
        serializer=studentserializer(stu,data=python_data,partial=True)     
        
        if serializer.is_valid():
            serializer.save()
            res={'msg':'update successful'}
            
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
              
            
            
        
    