from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    type = models.CharField(max_length=100, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)
    quality = models.IntegerField(null=False, blank=False)
    timestamp = models.DateField(auto_now=True)

    def __str__(self):
        return "name: " + str(self.name) + " type: " + str(self.type) + " time:" + str(self.timestamp)

class LoyalCustomer(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)

    timestamp = models.DateField(auto_now=True)

    products = models.ForeignKey("Product", on_delete=models.CASCADE, null=False, blank=False)


    def __str__(self):
        return "name: " + str(self.first_name)
