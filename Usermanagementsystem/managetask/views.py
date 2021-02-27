from django.shortcuts import render
from managetask.models import usertask
from managetask.serializers import usertaskSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from userRegistration.permissions import IsManagerUser
from userRegistration.models import User


# Create your views here.
class rolebasedTask(APIView):
    permission_classes = (permissions.IsAuthenticated,IsManagerUser,)

    def post(self,request):

        tasks = usertask.objects.create(
            user =  request.user,
            title = request.data.get('title'),
            blog = request.data.get('blog'),
            description = request.data.get('description'),
            status = request.data.get('status'),
            screenshot = request.data.get('screenshot'), 
        )
        return Response({"status":"datacreated","id":tasks.id},status=status.HTTP_201_CREATED)
    

    def get(self,request):
        user = request.user.id
        task_data = usertask.objects.filter(user = user)
        serializer = usertaskSerializer(task_data,many=True)
        return Response(serializer.data)

    def put(self,request):
        id = request.GET.get("id")
        if id:
            tasks = usertask.objects.filter(id=id).update(
                title = request.data.get('title'),
                blog = request.data.get('blog'),
                description = request.data.get('description'),
                status = request.data.get('status'),
                screenshot = request.data.get('screenshot')
            )
            return Response({"status":"record updated"})
        else:
            return Response({"status":"Not updated"},status=status.HTTP_304_NOT_MODIFIED)

    def delete(self,request):
        id = request.GET.get("id")
        if id:
            deletedata = usertask.objects.filter(id=id)
            deletedata.delete()
            return Response({"status":"CONTENT DELETED"})
        else:
            return Response({"status":"id required"},status=status.HTTP_400_BAD_REQUEST)

