from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from todos.models import TodoList
from todos.serializers import TodoListSerializer


# Create your views here.
@csrf_exempt
def todo_list(request):
    if request.method == 'GET':
        todo_lists = TodoList.objects.all()
        serializer = TodoListSerializer(todo_lists, many=True)

        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser.parse(request)
        serializer = TodoListSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)
