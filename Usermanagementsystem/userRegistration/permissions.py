from rest_framework.permissions import BasePermission
from userRegistration.models import User

class IsManagerUser(BasePermission):
    
    def has_permission(self,request,view):
            return request.user.role == 'Manager'

class IsUser(BasePermission):
    
    def has_permission(self,request,view):
            return request.user.role == 'user'
