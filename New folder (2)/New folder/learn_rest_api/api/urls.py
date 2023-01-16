from django.urls import path 
from .views import StudentListView
urlpatterns=[
    path("students/",StudentListView.as_view(),name="student"),
    path("students/<int:pk>",StudentListView.as_view(),name="student"),

]