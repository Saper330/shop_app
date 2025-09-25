from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from shop_app.models import Product, Order
from .shop_app_forms import OrderForm


def shop_index(request: HttpRequest):
    context = {

    }
    return render(request, 'shop_app/shop-index.html', context=context)


class ProductListView(ListView):
    template_name = "shop_app/products_list.html"
    model = Product
    context_object_name = "products"
    queryset = Product.objects.filter(archived=False)


class ProductDetailView(DetailView):
    template_name = "shop_app/product_detail.html"
    model = Product
    context_object_name = "product"


class ProductCreateView(CreateView):
    model = Product
    fields = "name", "description", "price", "discount"
    success_url = reverse_lazy("shop_app:products_list")


class ProductUpdateView(UpdateView):
    model = Product
    fields = "name", "description", "price", "discount"
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse(
            "shop_app:product_detail",
            kwargs={"pk": self.object.pk},
        )


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("shop_app:products_list")

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)


class OrdersListView(ListView):
    template_name = "shop_app/orders_list.html"
    model = Order
    context_object_name = "orders"


class OrderCreateView(CreateView):
    template_name = "shop_app/create_order.html"
    model = Order
    fields = "delivery_address", "promocode", "user", "products"
    success_url = reverse_lazy("shop_app:orders_list")


class OrderDetailView(DetailView):
    template_name = "shop_app/order_detail.html"
    model = Order
    context_object_name = "orders"


class OrderUpdateView(UpdateView):
    template_name = "shop_app/update_order.html"
    model = Order
    fields = "delivery_address", "promocode", "user", "products"

    def get_success_url(self):
        return reverse(
            "shop_app:order_detail",
            kwargs={"pk": self.object.pk},
        )


class OrderDeleteView(DeleteView):
    template_name = "shop_app/order_confirm_delete.html"
    model = Order
    success_url = reverse_lazy("shop_app:orders_list")

