from rest_framework import serializers

from ..models import Column

class ColumnSerializer(serializers.ModelSerializer):
    """Column serializer"""

    class Meta:
        model = Column
        fields = "__all__"
