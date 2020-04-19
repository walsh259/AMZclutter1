from django.db import models
# from django import Forms


class Trademark(models.Model):
    name = models.CharField(max_length=64)
    number = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id} {self.name} {self.number}"

class Shipmark(models.Model):
    category = models.CharField(max_length=64)
    number = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id} {self.category} {self.number}"
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
    ean = models.CharField(max_length=64, null=True, default=None)
    asin = models.CharField(max_length=64, null=True, default=None)
    trademark = models.ForeignKey(Trademark, null=True, default=None, on_delete=models.CASCADE, related_name="trademarks")
    weight = models.DecimalField(max_digits=8, decimal_places=2, null=True, default=None)
    length = models.DecimalField(max_digits=8, decimal_places=2, null=True, default=None)
    height = models.DecimalField(max_digits=8, decimal_places=2, null=True, default=None)
    width = models.DecimalField(max_digits=8, decimal_places=2, null=True, default=None)
    units_carton = models.DecimalField(max_digits=8, decimal_places=2, null=True, default=None)
    carton_weight = models.DecimalField(max_digits=8, decimal_places=2, null=True, default=None)
    carton_height = models.DecimalField(max_digits=8, decimal_places=2, null=True, default=None)
    carton_length = models.DecimalField(max_digits=8, decimal_places=2, null=True, default=None)
    carton_width = models.DecimalField(max_digits=8, decimal_places=2, null=True, default=None)
    shipmark = models.ForeignKey(Shipmark, null=True, default=None, on_delete=models.CASCADE, related_name="shipmarks")
    prep_fees = models.DecimalField(max_digits=8, decimal_places=2, null=True, default=None)
    lead_time = models.CharField(max_length=64, null=True, default=None)
    notes = models.TextField(max_length=100000,null=True)
    amazon_link = models.CharField(max_length=164, null=True, default=None)
    ebay_link = models.CharField(max_length=164, null=True, default=None)

    def __str__(self):
        return f"{self.id} {self.name} {self.sku} {self.unit_cost} {self.rrp} {self.average_fee} {self.shipping_fee} {self.agent} {self.ean} {self.asin} {self.trademark} {self.weight} {self.length} {self.height} {self.width} {self.units_carton} {self.carton_weight} {self.carton_height} {self.carton_length} {self.carton_width} {self.shipmark} {self.prep_fees} {self.lead_time} {self.notes} {self.amazon_link} {self.ebay_link}"

class Designer(models.Model):
    company = models.CharField(max_length=64)
    contact = models.CharField(max_length=64)
    email = models.CharField(max_length=128, blank = True)

    def __str__(self):
        return f"{self.id} {self.company} {self.contact} {self.email}"
