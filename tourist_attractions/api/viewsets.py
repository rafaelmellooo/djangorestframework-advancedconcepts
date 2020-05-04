from rest_framework.viewsets import ModelViewSet

from ..models import TouristAttraction
from .serializers import TouristAttractionSerializer


class TouristAttractionViewSet(ModelViewSet):
    queryset = TouristAttraction.objects.all()
    serializer_class = TouristAttractionSerializer
