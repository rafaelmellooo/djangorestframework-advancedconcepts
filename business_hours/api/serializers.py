from rest_framework.serializers import ModelSerializer
from ..models import BusinessHours


class BusinessHoursSerializer(ModelSerializer):
    class Meta:
        model = BusinessHours
        fields = ['id', 'weekday', 'opening_time', 'closing_time']
