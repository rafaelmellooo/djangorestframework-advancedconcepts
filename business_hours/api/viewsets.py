from rest_framework.viewsets import ModelViewSet
from ..models import BusinessHours
from .serializers import BusinessHoursSerializer


class BusinessHoursViewSet(ModelViewSet):
    queryset = BusinessHours.objects.all()
    serializer_class = BusinessHoursSerializer
