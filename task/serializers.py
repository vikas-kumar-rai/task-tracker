from rest_framework import serializers
from .models import Task, UpdateType, TaskTracker


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

    def validate(self, data):
        lst = [1, 2, 3, 4]
        if data['task'] not in lst:
            raise serializers.ValidationError("Wrong task, Please select 1 or 2 or 3 or 4.")
        return data


class TaskTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskTracker
        fields = "__all__"

    def validate(self, data):
        lst = [1, 2, 3, 4]
        check = TaskTracker.objects.filter(email=data['email'])
        for t in check:
            if t.task == data['task'] and t.update_type == data['update_type']:
                raise serializers.ValidationError("This Task tracker is already exist.")
        if data['task'] not in lst:
            raise serializers.ValidationError("Wrong task, Please select 1 or 2 or 3 or 4.")
        return data

