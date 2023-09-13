from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required

# Create your views here.

@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        login = request.data.get('login')
        password = request.data.get('password')
        print("LOGIN ", login)
        print("PASSWORD ", password)
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})

@login_required
@api_view(['POST'])
def login(request):

    return Response({
        'status': 'successfully logged in'
    })
