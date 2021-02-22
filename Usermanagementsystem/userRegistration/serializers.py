from rest_framework import serializers
from userRegistration.models import User
from django.contrib.auth.hashers import make_password


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','first_name','last_name','password','nationality','gender','date_joined')

    def create(self, validated_data):
        email = validated_data.pop("email", None)
        password = validated_data.pop("password", None)
        user = User.objects.create(email=email, password = make_password(password),**validated_data)
        return user
