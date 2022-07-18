from rest_framework import serializers
from accountapp.models import User


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'name', 'password',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user

class AccountDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'name', 'password',)
        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'required': False, 'write_only': True},
            'username': {'required': False},
        }

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        password = validated_data.get("password", instance.password)
        if not password.startswith("pbkdf2_sha256$"):
            instance.set_password(validated_data.get("password", instance.password))
        instance.email = validated_data.get("email", instance.email)
        instance.name = validated_data.get("name", instance.name)
        instance.save()

        return instance




