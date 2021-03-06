from managetask.models import usertask,subTask
from rest_framework import serializers

class subTaskSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = subTask
        fields = ('id','name','city','vote')

class usertaskSerializer(serializers.ModelSerializer):
    subtasks = subTaskSerializer(many=True,read_only=True)
    class Meta:
        model = usertask
        fields = '__all__'

    def create(self, validated_data):
        task_data = validated_data.pop('subtasks')
        subtask = usertask.objects.create(**validated_data)
        for task in task_data:
            return subTask.objects.create(subtask=subtask,**task)
        return subtask
    
    # def update(self, instance, validated_data):
    #     tasks_data = validated_data.pop('subtasks')
    #     # tasks = (instance.subtasks).all()
    #     # tasks = list(tasks)
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.blog = validated_data.get('blog', instance.blog)
    #     instance.save()
    #     keep_choices = []
    #     existing_ids = [c.id for c in instance.subtask_set]

    #     for task_data in tasks_data:
    #         if "id" in task_data.keys():
    #             if userTask.objects.filter(id=task_data["id"].exists()):
    #                 c = userTask.objects.get(id=task_data["id"])
    #                 c.text = task_data.get('text',c.text)
    #                 c.save()
    #             else:
    #                 continue
    #         else:
    #             c = userTask.objects.create(**task_data,artist = instance)
    #             keep_choices.append(c.id)


    # #     #     task = tasks.pop(0)
    # #     #     task.first_name = task_data.get('first_name', task.first_name)
    # #     #     task.last_date = task_data.get('last_name', task.last_name)
    # #     #     task.vote = task_data.get('vote', task.vote)
    # #     #     task.save()
    # #     # return instance

