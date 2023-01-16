from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

@api_view(['GET','POST'])
def student_details(request, id=None):
    if request.method == 'GET':
        if id is not None:
            if id % 2 != 0:
                return Response({"msg":"Your id must be even."}, status=status.HTTP_406_NOT_ACCEPTABLE)
            studentData = Student.objects.get(pk = id)
            serializerData = StudentSerializer(studentData)
            return Response(serializerData.data, status=status.HTTP_200_OK)
        studentData = Student.objects.all()
        serializerData = StudentSerializer(studentData, many=True)
        return Response(serializerData.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        data = request.data
        serializerData = StudentSerializer(data=data)
        if serializerData.is_valid():
            return Response({"msg":"Data created", "data":data}, status=status.HTTP_200_OK)
        return Response({"msg":"error"}, status=status.HTTP_406_NOT_ACCEPTABLE)
