from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from django.http import Http404
from .models import Student 
from .serializers import StudentSerializer
from rest_framework import status


class StudentListView(APIView):
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self,request,pk=None,format=None):
        if pk==None:
            queryset=Student.objects.all()
            serializer=StudentSerializer(queryset,many=True)

        else:
            queryset=Student.objects.filter(id=pk).last()
            serializer=StudentSerializer(queryset)

        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self,request,id,format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)