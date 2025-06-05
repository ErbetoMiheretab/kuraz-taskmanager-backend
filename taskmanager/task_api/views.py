from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSer


@api_view(["GET"])
def index(request):
    return render(request, "tasks/index.html")


#List all 
@api_view(["GET"])
def list_tasks(request):
    tasks = Task.objects.all()
    serializer = TaskSer(tasks, many=True)
    return Response(serializer.data)


#Create a new task
@api_view(["POST"])
def create_task(request):
    serializer = TaskSer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#get by id
@api_view(["GET"])
def get_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    serializer = TaskSer(task)
    return Response(serializer.data)


#mark complete
@api_view(["PUT"])
def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    serializer = TaskSer(task)
    return Response(serializer.data)


#Delete a task
@api_view(["DELETE"])
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
