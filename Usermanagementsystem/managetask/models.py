from django.db import models
from userRegistration.models import User

STATUS = (("GOOD","GOOD"),("OK","OK"),("BAD","BAD"))

# Create your models here.
class usertask(models.Model):
    title = models.CharField(max_length=50,default=None)
    blog = models.CharField(max_length=100,default=None)
    description = models.TextField(max_length=250,null=True)
    status = models.CharField(max_length=50,choices=STATUS,null=True,blank=True)
    screenshot = models.ImageField(null = True,blank=True)
    created = models.DateField(auto_now=True)
    updated = models.DateField(auto_now=True)
    user = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
