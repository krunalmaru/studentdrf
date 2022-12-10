from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .serializer import studentSerializer
from rest_framework.renderers import JSONRenderer
# Create your views here.

def student(request):
    stu = Student.objects.get(roll=102)  #complex datatype
    serializer = studentSerializer(stu)  #python datatype
    json_data = JSONRenderer().render(serializer.data) # json data
    return HttpResponse(json_data, content_type = 'application/json')


