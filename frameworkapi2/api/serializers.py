from rest_framework.serializers import ModelSerializer
from frameworkapi2.models import JsonPlaceholder

class JsonSerializer(ModelSerializer):
    """Serializer para representar os dados na api"""

    class Meta:
        model = JsonPlaceholder
        fields = ('userId', 'id', 'title', 'completed')
