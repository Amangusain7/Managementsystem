from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self, email=None, password=None, **validated_data):
        user = self.model(email=email, **validated_data)
        user.set_password(password)
        user.is_staff = False
        user.is_active = True
        user.is_superuser = False 
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **validated_data):
        user = self.create_user(email,password=password,**validated_data)

        user.is_staff = True
        user.is_active = True
        user.is_superuser = True 
        user.save(using=self._db)
        return user


    def create_staffuser(self, email,  password=None):
        user = self.create_user(email,password=password
        )
        user.is_admin = False
        user.is_staff = True
        user.is_superuser = False 
        user.save(using=self._db)
        return user
