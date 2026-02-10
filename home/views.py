from django.shortcuts import render
from django.http import JsonResponse ,HttpResponse
from django.views.decorators.csrf import csrf_exempt # 1. Import karein
import json
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.response import Response
from .models import Student
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate, login


@api_view(["POST"])
def signup(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if not username or not password:
        return Response(
            {"error": "username and password required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    if User.objects.filter(username=username).exists():
        return Response(
            {"error": "user already exists"},
            status=status.HTTP_400_BAD_REQUEST
        )

    user = User.objects.create_user(
        username=username,
        password=password
    )

    return Response(
        {"message": "user created"},
        status=status.HTTP_201_CREATED
    )



from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)

    if not user:
        return Response(
            {"error": "invalid credentials"},
            status=status.HTTP_401_UNAUTHORIZED
        )

    token, created = Token.objects.get_or_create(user=user)

    return Response({
        "token": token.key
    })


# @api_view(["POST"])
# def login_session(request):
#     username = request.data.get("username")
#     password = request.data.get("password")

#     if not username or not password:
#         return Response(
#             {"error": "username and password required"},
#             status=status.HTTP_400_BAD_REQUEST
#         )

#     user = authenticate(username=username, password=password)

#     if not user:
#         return Response(
#             {"error": "invalid credentials"},
#             status=status.HTTP_401_UNAUTHORIZED
#         )

#     #  YAHI SESSION CREATE HOTA HAI
#     login(request, user)

#     return Response({
#         "message": "login successful (session created)"
#     })




def Home(request) :
    return  JsonResponse({
        "hello" : "hi mahesh"
    })


def  About(request) :
    return  HttpResponse("<h1>welcome my about page</h1>") 


@csrf_exempt
def Test_data(request) :
    if request.method == "GET":
        return JsonResponse({
            "hi" :"this is get"
        })
    
    if request.method == "POST" :
        return JsonResponse({
            "hi":"this is post"
        })    

@csrf_exempt
def Echo_api(request):
    if request.method == "POST":
        data = json.loads(request.body)
        
        return JsonResponse({
            "yes": data
        }) 
        
        
        
@api_view(["GET" ,"POST"])
@permission_classes([IsAuthenticated])
def Easy_api(request):
    if request.method == "GET":
        return Response({
            "msg":"working"
        })        
    
    if request.method == "POST" :
        return Response({
            "hay":"good work"
        })    
        
        
@api_view(["GET","POST"])
@permission_classes([IsAuthenticated])
def Student_all(request):
    if request.method == "GET":
        students = Student.objects.all()
        
        data = []
        for i in students :
            data.append({
                "name":i.name,
                "age ":i.age
            })
        return Response(data)

    if request.method == "POST":
        name = request.data.get("name")
        age = request.data.get("age")
        
        
        if not name or not age:
            return Response(
                {
                    "error" :"name and age  are require"
                },
                status=status.HTTP_400_BAD_REQUEST
            )  
            
        students = Student.objects.create(
            name = name,
            age = age
        )      
        return Response({
            "name":students.name,
            "age":students.age
        },
          status=status.HTTP_201_CREATED
                        
       )    