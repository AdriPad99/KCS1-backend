from django.shortcuts import render
from rest_framework import generics
from .models import Tasks
from .serializers import TasksSerializer

#  for listing all the tasks or making a new one
class TasksLC(generics.ListCreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer

# for getting, updating, or deleting a task from a provided integer
class TasksRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer