from rest_framework import viewsets, permissions

from users.models import Address
from users.serializers.address_serializer import AddressSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.AllowAny]
