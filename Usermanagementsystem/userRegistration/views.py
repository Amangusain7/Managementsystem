from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import status
from userRegistration.models import User
from userRegistration.serializers import UserRegisterSerializer
from rest_framework.permissions import IsAuthenticated
from userRegistration.authenticate import UserAuthentication

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

    def put(self,request):
        email = request.GET.get('email')
        li = User.objects.get(email=email)
        serializer = UserRegisterSerializer(li,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"modified","data":serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):

    def post(self, request):

        user = UserAuthentication().authenticate(email=request.data.get("email"), password=request.data.get("password"))
        
        if user is not None:
            try:
                token = Token.objects.get(user_id=user.id)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)
            return Response(token.key)
        else:
            return Response([], status=status.HTTP_401_UNAUTHORIZED)


        