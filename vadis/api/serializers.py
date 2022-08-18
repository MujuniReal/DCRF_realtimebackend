import email
from unicodedata import name
from rest_framework import serializers
from django.contrib.auth.models import User
from vadis.models import Vadis

"""class VadisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vadis
        fields = "__all__"

    def create(self,validated_data):
        vadis = Vadis(name=validated_data['name'],
        description=validated_data['description'])
        vadis.save()
        return vadis """

class VadisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vadis
        fields = "__all__"
        #extra_kwargs = {'password': {'write_only': True}}

    def create(self,validated_data):
        user = Vadis(
            
            name=validated_data['name'],
            description = validated_data['description']
        )
        #user.set_password(validated_data['password'])
        user.save()
        return user