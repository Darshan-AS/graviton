from rest_framework import viewsets, permissions

from users.models import Lender
from users.serializers.lender_serializer import LenderSerializer


class LenderViewSet(viewsets.ModelViewSet):
    queryset = Lender.objects.all()
    serializer_class = LenderSerializer
    permission_classes = [permissions.AllowAny]