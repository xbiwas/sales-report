from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=120)
    logo = models.ImageField(upload_to='customer', default='img.jpg')
    
    def __str__(self):
        return str(self.name)
    

