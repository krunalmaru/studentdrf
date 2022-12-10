from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .serializer import studentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
# Create your views here.

def student_a(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id',None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = studentSerializer(stu)  #python datatype
            json_data = JSONRenderer().render(serializer.data) # json data
            return HttpResponse(json_data, content_type = 'application/json')
        stu = Student.objects.all()
        serializer = studentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type = 'application/json')

