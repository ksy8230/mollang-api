from django.http import Http404
from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from companyapp.models import Company
from companyapp.serializers import CompanySerializer, CompanyUpdateSerializer
from rest_framework.generics import get_object_or_404

# 업체 등록
class RegisterCompany(APIView):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 업체 수정
class UpdateCompany(APIView):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, pk):
        company = get_object_or_404(Company, pk=pk)
        print(company)
        return company

    def put(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        saved_company = self.get_object(pk)
        # print(saved_company)
        serializer = CompanyUpdateSerializer(instance=saved_company, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 업체 리스트 조회
class CompanyList(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        print(serializer)
        return Response(serializer.data)
