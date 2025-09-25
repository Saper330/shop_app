from django.contrib import admin

from .models import Product, Order


class OrderInline(admin.StackedInline):
    model = Product.orders.through


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        OrderInline,
    ]
    list_display = "pk", "name", "description", "price", "discount"
    list_display_links = "pk", "name"
    ordering = "pk",
    search_fields = "name", "pk"

    def description_short(self, obj: Product) -> str:
        if obj.description < 50:
            return obj.description
        return obj.description[:50] + '...'


class ProductInline(admin.StackedInline):
    model = Order.products.through


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        ProductInline,
    ]
    list_display = "pk", "delivery_address", "promocode", "created_at", "user_verbose"
    list_display_links = "pk",
    search_fields = "delivery_address", "pk"

    def get_queryset(self, request):
        return Order.objects.select_related("user").prefetch_related("products")

    def user_verbose(self, obj: Order) -> str:
        return obj.user.first_name or obj.user.username
