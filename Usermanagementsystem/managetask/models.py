from django.db import models
from userRegistration.models import User
import datetime
from django.utils import timezone

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

    # @property
    # def subtasks(self):
    #     return self.subtask_set.all()

class subTask(models.Model):
    subtask = models.ForeignKey(usertask,related_name='subtasks',default=None,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    vote = models.IntegerField(default=0)
