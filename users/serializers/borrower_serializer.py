from rest_framework import serializers

from users.models import Borrower


class BorrowerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Borrower
        fields = ('id', 'name', 'gender', 'dob', 'email', 'phone', 'address')
