from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *

@api_view(['GET', 'POST', 'PATCH'])
def home(request):
    if request.method == 'GET':
        return Response({
            'status' : 200,
            'message' : 'GET message is success'
        })
    elif request.method == 'POST':
        return Response({
            'status' : 200,
            'message' : 'POST message is success'
        })
    elif request.method == 'PATCH':
        return Response({
            'status' : 200,
            'message' : 'PATCH message is success'
        })
    else:
        return Response({
            'status' : 400,
            'message' : 'No proper request method'
        })

@api_view(['POST'])   
def post_todo(request):
    try:
        data = request.data
        # print(data)
        serializer = TodoSerializer(data= data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response({
                'status' : True,
                'message' : 'Serializer fields matched :) !!',
                'errors' : serializer.errors
            })

        return Response({
            'status' : False,
            'message' : 'Serializer fields not matched!!',
            'errors' : serializer.errors
        })

    except Exception as e:
        print(e)
        return Response({
            'status' : False,
            'message' : 'exception here something went wrong!!'
        })
    

@api_view(['GET'])
def get_todo(request):
    try:
        todo_objs = Todo.objects.all()
        serializer = TodoSerializer(todo_objs, many= True)
        return Response({
            'status': True,
            'message': 'Todo Fetched',
            'data': serializer.data
        })
    except Exception as e:
        print(e)
        return Response({
            'status': False,
            'message': 'Todo not Fetched',
        })