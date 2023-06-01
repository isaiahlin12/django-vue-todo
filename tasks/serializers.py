from rest_framework import routers, serializers, viewsets
from .models import Task

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'status', 'due_date', 'completed_on']