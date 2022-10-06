from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class MyOrder(models.Model):
    description = models.CharField(max_length=512)
    product = models.ManyToManyField(Product, through='ProductMyOrder')

    def __str__(self):
        return self.description

class ProductMyOrder(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    my_order = models.ForeignKey(MyOrder, on_delete=models.CASCADE)

    def __str__(self):
        return f"my_order: {self.my_order}, product: {self.product}, quantity: {self.quantity}, price: {self.price}"

