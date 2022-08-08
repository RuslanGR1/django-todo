from ..serializers import ColumnSerializer
from ..models import Column

from rest_framework import viewsets


class ColumnViewSet(viewsets.ModelViewSet):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer
