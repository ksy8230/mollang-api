from rest_framework import serializers
from companyapp.models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'categories', 'region', 'phone', 'siteUrl', 'created_at', 'username')

    def create(self, validated_data):
        company = Company.objects.create(**validated_data)
        return company


class CompanyUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'categories', 'region', 'phone', 'siteUrl', 'created_at', 'username')

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.categories = validated_data.get("categories", instance.categories)
        instance.region = validated_data.get("region", instance.region)
        instance.phone = validated_data.get("phone", instance.phone)
        instance.siteUrl = validated_data.get("siteUrl", instance.siteUrl)
        instance.save()

        return instance
