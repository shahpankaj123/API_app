from django.urls import path
from .views import *

urlpatterns = [
    path('student/<int:cid>',studentdetail,name='home'),
    path('',student_all),
    path('student_create/',student_create),
    path('student_api/',student_api),
]