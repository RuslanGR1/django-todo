from rest_framework import viewsets

from ..serializers import TaskSerializer
from ..models import Task, Column


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.all()
        columnId = self.request.query_params.get('columnId')
        if columnId:
            column = Column.objects.get(pk=columnId)
            return queryset.filter(column=column)
        else:
            return queryset
