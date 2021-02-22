from rest_framework import serializers
from userRegistration.models import User
from django.contrib.auth.hashers import make_password


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','first_name','last_name','password','nationality','gender','date_joined','profile_image')

    def create(self, validated_data):
        email = validated_data.pop("email", None)
        password = validated_data.pop("password", None)
        user = User.objects.create(email=email, password = make_password(password),**validated_data)
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username',instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.password = validated_data.get('password', instance.password)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.nationality = validated_data.get('nationality', instance.nationality)
        instance.date_joined = validated_data.get('date_joined', instance.date_joined)
        instance.profile_image = validated_data.get('profile_image',instance.profile_image)

        instance.save()
        return instance