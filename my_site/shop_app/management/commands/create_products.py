from django.contrib.auth.models import User
from django.core.management import BaseCommand

from shop_app.models import Product


class Command(BaseCommand):
    """
    Created product
    """
    def handle(self, *args, **options):
        self.stdout.write("Creation product..")
        products = [
            ('BMW', 35000),
            ('Audi', 36080.555),
            ('Mersedes', 35100),
            ('Mitsubishi', 55000)
        ]
        for product in products:
            product, created = Product.objects.get_or_create(name=product[0], price=product[1])
            self.stdout.write(f'Product {product.name} created!')
        self.stdout.write(self.style.SUCCESS("Products created!"))
