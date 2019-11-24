from rest_framework import serializers

from users.models.lender import Lender


class LenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lender
        fields = ('id', 'name', 'email', 'gender', 'dob', 'phone')
