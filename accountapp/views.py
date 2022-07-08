from rest_framework.views import APIView
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from accountapp.serializers import AccountSerializer
from django.contrib.auth import authenticate, login
from .models import User
from django.shortcuts import render

def hello_world(request):
    return Response('Hello world!')

# 회원가입
class CreateAccount(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 로그인 
class Login(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data

        username = data.get('username', None)
        password = data.get('password', None)

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({'message': "User logged in successully", 'data': user.id})
        else:
            return Response({'message': "User does not exits"}, status=400)

# 유저들 조회
class AccountList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = AccountSerializer(users, many=True)
        return Response(serializer.data)

