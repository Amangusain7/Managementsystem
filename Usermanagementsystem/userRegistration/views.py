from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import authenticate
from userRegistration.serializers import UserRegisterSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class registeruser(APIView):
    
    def post(self,request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()    
            if user: 
                token = Token.objects.create(user=user)
                return Response({"token":token.key},status=status.HTTP_201_CREATED)
            else:
                return Response([],status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        