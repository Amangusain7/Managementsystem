from userRegistration.models import User
from rest_framework import authentication
from rest_framework import exceptions
from django.contrib.auth import authenticate, get_user_model

class UserAuthentication(authentication.BaseAuthentication):
    def authenticate(self,email=None,password=None):
        if not email or not password:
            return None
        try:
            user = User.objects.get(email=email)
            password = user.check_password(password)

        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')
        return user
    