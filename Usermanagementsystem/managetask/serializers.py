from managetask.models import usertask
from rest_framework import serializers


class usertaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = usertask
        fields = '__all__'
