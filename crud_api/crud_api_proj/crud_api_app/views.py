from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from django.http import JsonResponse
# Create your views here.

def student_details(request):
    studentData = Student.objects.all()
    serializerData = StudentSerializer(studentData)
    return JsonResponse(serializerData.data, safe=False)
