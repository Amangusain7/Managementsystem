from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .manager import UserManager

GENDER_CHOICES = (("Male","Male"),("female","female"))
ROLE = (("admin","admin"),("user","user"),("manager","manager"))

# Create your models here.
class User(AbstractBaseUser,PermissionsMixin):
   
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100,null=True,blank=True,default=None)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100,null=True,blank=True,default=None)
    last_name = models.CharField(max_length=100,null=True,blank=True,default=None)
    password = models.CharField(max_length=100,default=None)
    nationality = models.CharField(max_length=100,null=True,blank=True)
    gender = models.CharField(max_length=100,choices=GENDER_CHOICES,null=True,blank=True)
    date_joined = models.DateTimeField(auto_now=True)
    profile_image = models.ImageField('profile picture', null=True, blank=True)
    role = models.CharField(max_length=50, choices=ROLE, null=True,default=None)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email