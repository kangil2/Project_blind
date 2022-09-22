from django.db import transaction
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

User = get_user_model()

class SignUpSerializer(ModelSerializer):
    class Meta:
        model  = User
        fields = '__all__'
        extra_kwargs = {
            'last_login' : {'read_only' : True}
        }

    def create(self, validated_data):
        email    = validated_data.get('email')
        nickname = validated_data.get('nickname')
        password = validated_data.get('password')
        company  = validated_data.get('company')
        
        user = User(
            email    = email,
            nickname = nickname,
            company  = company
        )
        user.set_password(password)
        user.save()
        return user