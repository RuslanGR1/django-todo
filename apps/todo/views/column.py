from rest_framework import viewsets

from ..serializers import ColumnSerializer
from ..models import Column, Board


class ColumnViewSet(viewsets.ModelViewSet):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer

    def get_queryset(self):
        queryset = Column.objects.all()
        boardId = self.request.query_params.get('boardId')
        if boardId:
            board = Board.objects.get(pk=boardId)
            return queryset.filter(board=board)
        else:
            return queryset
