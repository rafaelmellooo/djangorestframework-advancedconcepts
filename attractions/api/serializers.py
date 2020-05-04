from rest_framework.serializers import ModelSerializer
from ..models import Attraction


class AttractionSerializer(ModelSerializer):
    class Meta:
        model = Attraction
        fields = ['id', 'name', 'description', 'minimum_age', 'business_days']
