from rest_framework.viewsets import ModelViewSet
from .serializers import JsonSerializer
from frameworkapi2.models import JsonPlaceholder
from rest_framework.permissions import IsAuthenticated

class JsonViewset(ModelViewSet):
    queryset = JsonPlaceholder.objects.all()
    serializer_class = JsonSerializer
    permission_classes = (IsAuthenticated,)