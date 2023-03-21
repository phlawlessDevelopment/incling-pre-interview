from django import urls
from .viewsets import TaskViewSet, TileViewSet
urlpatterns = [
    urls.path('tasks/', TaskViewSet.as_view({'get': 'list'})),
    urls.path('tasks/<int:pk>/', TaskViewSet.as_view({'get': 'retrieve'})),
    urls.path('tiles/', TileViewSet.as_view({'get': 'list'})),
    urls.path('tiles/<int:pk>/', TileViewSet.as_view({'get': 'retrieve'})),
        ]
