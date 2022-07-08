from rest_framework import serializers
from accountapp.models import User


class AccountSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'name', 'password')


