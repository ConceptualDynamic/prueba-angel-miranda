from dataclasses import fields
from pyexpat import model
from rest_framework import serializers

from .models import Client,Product

# NOTA:

# {
#     "username": "admin",
#     "password": "Password@123"
# }
# pip install -r  requirements.txt
from django.contrib.auth.models import User

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user




class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields  = ('first_name','last_name','Birth','dni','Phone','direccion','email','status',)
        read_only_fields = ('created_at',)

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields  = ('name','quantity','description','unit_price','image','status')
        read_only_fields = ('created_at',)
