from django.contrib.auth.models import User
from django.core.management import BaseCommand

from shop_app.models import Product, Order


class Command(BaseCommand):
    """
    Created order
    """
    def handle(self, *args, **options):
        self.stdout.write("Creation order..")
        user = User.objects.get(username='admin')
        order = Order.objects.get_or_create(
            delivery_address='Vinokurova 170',
            promocode='ASSA',
            user=user,
        )
        self.stdout.write(f"Order {order} created!")
