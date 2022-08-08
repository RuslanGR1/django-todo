from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    TaskViewSet,
    BoardViewSet,
    ColumnViewSet,
)


router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'boards', BoardViewSet, basename='board')
router.register(r'columns', ColumnViewSet, basename='column')

urlpatterns = (
    path("", include(router.urls)),
)
