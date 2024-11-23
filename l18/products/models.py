from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    quantity = models.IntegerField()
    quality = models.IntegerField()
    timestamp = models.DateField(auto_now=True)

    def __str__(self):
        return "name: " + str(self.name) + " type: " + str(self.type) + " time:" + str(self.timestamp)