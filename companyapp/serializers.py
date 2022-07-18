from rest_framework import serializers
from companyapp.models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'categories', 'region', 'phone', 'siteUrl', 'created_at')
