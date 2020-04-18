from django.db import models

# Create your models here.
class Supplier(models.Model):
    company = models.CharField(max_length=64)
    contact = models.CharField(max_length=64)
    email = models.CharField(max_length=128, blank = True)

    def __str__(self):
        return f"{self.id} {self.company} {self.contact} {self.email}"

class Product(models.Model):
    name = models.CharField(max_length=64)
    sku = models.CharField(max_length=64, blank = True)
    unit_cost = models.DecimalField(max_digits=8, decimal_places=2)
    rrp = models.DecimalField(max_digits=8, decimal_places=2)
    average_fee = models.DecimalField(max_digits=8, decimal_places=2)
    shipping_fee = models.DecimalField(max_digits=8, decimal_places=2)
    agent = models.ForeignKey(Supplier, null=True, default=None, on_delete=models.CASCADE, related_name="suppliers")



    def __str__(self):
        return f"{self.id} {self.name} {self.sku} {self.unit_cost} {self.rrp} {self.average_fee} {self.shipping_fee}"
