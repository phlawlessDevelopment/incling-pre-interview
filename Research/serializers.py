from rest_framework import serializers
from .models import Task, Tile


class TaskReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'description', 'order', '_type', 'tile')

class TileReadSerializer(serializers.ModelSerializer):
    tasks = TaskReadSerializer(many=True, read_only=True)
    class Meta:
        model = Tile
        fields = ('launch_date', 'status', 'tasks')

class TaskWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'description', 'order', '_type', 'tile')

class TileWriteSerializer(serializers.ModelSerializer):
    tasks = TaskWriteSerializer(many=True, read_only=True)
    class Meta:
        model = Tile
        fields = ('launch_date', 'status', 'tasks')
