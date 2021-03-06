from rest_framework.permissions import BasePermission
from userRegistration.models import User

class IsManagerUser(BasePermission):
    
    def has_permission(self,request,view):
            return request.user.role == 'manager'
                
# class AdminsPermissions(BasePermission):
#     allowed_user_roles = (User.role)
#     def has_permission(self, request, view):
#         is_allowed_user = request.user.role in allowed_user_roles
#         return is_allowed_user


    