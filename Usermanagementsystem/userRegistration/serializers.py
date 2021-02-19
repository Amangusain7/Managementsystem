from rest_framework import serializers
from userRegistration.models import User
from django.contrib.auth.hashers import make_password


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        print("888888888888888888888888888888888888888")
        model = User
        fields = ('username','email','first_name','last_name','password','nationality','gender','date_joined')
        #fields = '__all__'

    def create(self, validated_data):
        print("13333333333333333333333333333")
        password = serializers.CharField(write_only=True, required=True)
        email = validated_data.pop("email", None)
        password = validated_data.pop("password", None)
        print("155555555555555555555555555",email,"1777777777777777777777",password)
        user = User.objects.create(email=email, password = make_password(password),**validated_data)
        return user
