from rest_framework import serializers

from users.models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'door_no', 'street', 'locality', 'landmark', 'city', 'state', 'country', 'pin_code')
