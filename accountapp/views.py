from rest_framework.views import APIView
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from accountapp.serializers import AccountSerializer
from django.contrib.auth import authenticate, login
from .models import User
from django.shortcuts import render
# Create your views here.
# AccountList: 유저 생성, 유저 수정, 유저 삭제, 유저 조회
# AccountLists: 유저들 조회
# Login : 로그인

def hello_world(request):
    return Response('Hello world!')

class AccountList(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AccountSerializer



class Login(APIView):
    # 로그인
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data

        username = data.get('username', None)
        password = data.get('password', None)

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({'detail': "Success"})

