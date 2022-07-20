from django.http import Http404
from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from companyapp.models import Company
from companyapp.serializers import CompanySerializer
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
        return company

    def put(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        saved_company = self.get_object(pk)
        serializer = CompanySerializer(instance=saved_company, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        saved_company = self.get_object(pk)
        saved_company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# 업체 리스트 조회
class CompanyList(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        search_type = request.GET.get("searchType", None)

        try:
            if search_type == "name":
                name = request.GET.get("searchValue", None)
                queryset = Company.objects.filter(name=name).order_by("-created_at", "-id")
            elif search_type == "categories":
                categories = request.GET.get("searchValue", None)
                queryset = Company.objects.filter(categories__icontains=categories).order_by("-created_at", "-id")
            elif search_type == "region":
                region = request.GET.get("searchValue", None)
                queryset = Company.objects.filter(region=region).order_by("-created_at", "-id")
            elif search_type == "username":
                username = request.GET.get("searchValue", None)
                queryset = Company.objects.filter(username=username).order_by("-created_at", "-id")
            else:
                queryset = Company.objects.order_by("-created_at", "-id")
            serializer = CompanySerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)


        # companies = Company.objects.all()
        # serializer = CompanySerializer(companies, many=True)
        # return Response(serializer.data)
