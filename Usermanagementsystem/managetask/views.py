from django.shortcuts import render
from managetask.models import usertask,subTask
from managetask.serializers import usertaskSerializer,subTaskSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from userRegistration.permissions import IsManagerUser
from userRegistration.models import User
from django.http import HttpResponse, Http404
from rest_framework import viewsets

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
        task_data = usertask.objects.filter(user = user).order_by(self.request.GET['order_by'])
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

           
class subtask(APIView):

    def post(self,request):
        serializer = subTaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # return Response({"id":subtasks.id},status=status.HTTP_201_CREATED)

    def get(self,request):
        subtask = subTask.objects.all()
        serializer = subTaskSerializer(subtask,many=True)
        return Response(serializer.data)


    def put(self,request):
        id = request.GET.get('id')
        subtask = subTask.objects.filter(id=id).update(
            first_name = request.data.get('first_name'),
            last_name = request.data.get('last_name')
        )
        return Response({"status":"record updated"})

    def delete(self,request):
        deletedata = subTask.objects.all()
        deletedata.delete()
        return Response({"status":"CONTENT DELETED"})
        # else:
        #     return Response({"status":"id required"},status=status.HTTP_400_BAD_REQUEST)



