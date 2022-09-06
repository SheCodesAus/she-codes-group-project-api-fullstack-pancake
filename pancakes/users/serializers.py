from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.hashers import make_password

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    profile_image = serializers.CharField(max_length=500, default='./pancakes/images/Dandelion.png')

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return CustomUser.objects.create(**validated_data)

class CustomUserDetailSerializer(CustomUserSerializer):

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        if "password" in validated_data.keys():
            instance.password = make_password(validated_data.get('password'))
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.profile_image = validated_data.get('profile_image', instance.profile_image)
        instance.save()
        return instance