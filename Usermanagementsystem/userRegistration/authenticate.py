from userRegistration.models import User
from rest_framework import authentication
from rest_framework import exceptions
from django.contrib.auth import authenticate

class UserAuthentication(authentication.BaseAuthentication):
    def authenticate(self,email=None,password=None):
        if not email or not password:
            return None
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
            else:
                return None
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('Something went wrong')

                
    