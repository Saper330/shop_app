from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    class Meta:
        pass
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    archived = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"Product(name={self.name!r})"


class Order(models.Model):
    class Meta:
        pass
    delivery_address = models.TextField(null=True, blank=True)
    promocode = models.CharField(blank=True, max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product, related_name="orders")

    def __str__(self) -> str:
        return f"Order(pk={self.pk})"

