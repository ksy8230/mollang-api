from rest_framework import serializers
from reviewapp.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='username.name')
    class Meta:
        model = Review
        fields = ('id', 'name', 'categories', 'region', 'title', 'content', 'rate', 'updated_at', 'username')

    def create(self, validated_data):
        company = Review.objects.create(**validated_data)
        return company

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get("name", instance.name)
    #     instance.categories = validated_data.get("categories", instance.categories)
    #     instance.region = validated_data.get("region", instance.region)
    #     instance.phone = validated_data.get("phone", instance.phone)
    #     instance.siteUrl = validated_data.get("siteUrl", instance.siteUrl)
    #     instance.save()
    #     return instance
#
