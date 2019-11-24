from django.db import models


class Address(models.Model):
    door_no = models.CharField(max_length=10, null=True)
    street = models.CharField(max_length=100, null=True)
    locality = models.CharField(max_length=100, null=True)
    landmark = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    pin_code = models.CharField(max_length=6, null=True)
    
    def __str__(self):
        return f'{self.id}: {self.door_no} {self.street} {self.locality}, near {self.landmark}, ' \
               f'{self.city} {self.state} {self.country} - {self.pin_code}'
