from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
# from userRegistration.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from userRegistration.serializers import UserRegisterSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class registeruser(APIView):
    def post(self,request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
        
        # if serializer is not None: 
        #     token = Token.objects.create(user=serializer)
        #     return Response(token.key)
        # else:
        #     return Response([],status = status.HTTP_400_BAD_REQUEST)
        
        return Response({"status":"data created"})

        