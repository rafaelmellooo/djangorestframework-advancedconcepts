from rest_framework.serializers import ModelSerializer
from ..models import Address


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'country', 'uf', 'city', 'neighborhood', 'street', 'number', 'latitude', 'longitude']
