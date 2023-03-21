from rest_framework import viewsets
from .models import Task, Tile
from .serializers import TaskReadSerializer, TaskWriteSerializer, TileReadSerializer, TileWriteSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskReadSerializer

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return TaskWriteSerializer
        return TaskReadSerializer

class TileViewSet(viewsets.ModelViewSet):
    queryset = Tile.objects.all()
    serializer_class = TileReadSerializer

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return TileWriteSerializer
        return TileReadSerializer
