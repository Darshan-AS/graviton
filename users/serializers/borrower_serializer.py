from rest_framework import serializers

from users.models import Borrower
from users.serializers.address_serializer import AddressSerializer


class BorrowerSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    
    class Meta:
        model = Borrower
        fields = ('id', 'name', 'gender', 'dob', 'email', 'phone', 'address')
    
    def create(self, validated_data):
        address_serializer = self.fields['address']
        address_validated_data = validated_data.pop('address')
        address = address_serializer.create(address_validated_data)
        
        validated_data['address'] = address
        return super(BorrowerSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        address_serializer = self.fields['address']
        address_validated_data = validated_data.pop('address')
        address_serializer.update(instance.address, address_validated_data)

        return super(BorrowerSerializer, self).update(instance, validated_data)