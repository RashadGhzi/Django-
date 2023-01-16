from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated,DjangoModelPermissionsOrAnonReadOnly
from rest_framework import viewsets
# Create your views here.
class StudentDetails(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly,IsAuthenticated]

def index(request):
    return render(request, 'jwt_app/index.html')
