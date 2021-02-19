from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import PermissionsMixin
#from django.contrib.auth.models import User
from .manager import UserManager
from django.utils import timezone

# Create your models here.
class User(AbstractBaseUser,PermissionsMixin):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100,null=True,blank=True,default=None)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=100,null=True,blank=True,default=None)
    last_name = models.CharField(max_length=100,null=True,blank=True,default=None)
    password = models.CharField(max_length=100,default=None)
    nationality = models.CharField(max_length=100,null=True,blank=True)
    gender = models.CharField(max_length=100,null=True,blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email