import datetime
from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=50, default=True)
    last_name = models.CharField(max_length=50, default=True)
    date_of_birth = models.DateField(default=datetime.date.today)
    gender = models.CharField(max_length=10, default=True)
    country = models.CharField(max_length=50, default='default_country')
    state_district = models.CharField(max_length=50, default=True)
    town = models.CharField(max_length=50, default=True)
    zip_code = models.CharField(max_length=10, default=True)
    phone_number = models.CharField(max_length=15, default=True)
    email = models.EmailField(max_length=200, default=True)
    
    
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.date_of_birth + ' ' + self.gender + ' ' + self.country + ' ' + self.state_district + ' ' + self.town + ' ' + self.zip_code + ' ' + self.phone_number_1 + ' ' + self.phone_number_2 + ' ' + self.email 

 
    
     