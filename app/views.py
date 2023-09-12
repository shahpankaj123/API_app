from django.shortcuts import render
from django.http import HttpResponse
from .models import student
from .serializer import *
from rest_framework.renderers import JSONRenderer



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
