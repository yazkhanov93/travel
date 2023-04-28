from rest_framework import serializers
from task.models import *


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["title","point"]


class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class TaskDoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskDone
        fields = ["task", "user", "checked"]


class TaskDoneDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskDone
        fields = "__all__"