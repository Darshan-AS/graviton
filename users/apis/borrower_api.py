from rest_framework import viewsets, permissions

from users.models import Borrower
from users.serializers.borrower_serializer import BorrowerSerializer


class BorrowerViewSet(viewsets.ModelViewSet):
    queryset = Borrower.objects.all()
    serializer_class = BorrowerSerializer
    permission_classes = [permissions.AllowAny]
