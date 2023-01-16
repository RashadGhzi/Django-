from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from .serilizer import SerializerStudent
from .models import Student
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET', 'POST'])

def item(request):
    if request.method == "POST":
        stu = Student.objects.all()
        print(stu)
        serializer = SerializerStudent(stu, many=True)
        print(serializer.data)
        # jsonData = JSONRenderer().render(serializer.data)
        # print(jsonData)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SerializerStudent(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
