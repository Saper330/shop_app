from django.urls import path
from .views import (ShopIndexViev,
                    ProductListView,
                    ProductDetailView,
                    OrdersListView,
                    OrderCreateView,
                    OrderDetailView,
                    ProductCreateView,
                    ProductUpdateView,
                    ProductDeleteView,
                    OrderDeleteView,
                    OrderUpdateView,
                    
                    )


app_name = 'shop_app'

urlpatterns = [
    
    path('', ShopIndexViev.as_view(), name='index'),
    path('products/', ProductListView.as_view(), name='products_list'),
    path('orders/', OrdersListView.as_view(), name='orders_list'),
    path('orders/create/', OrderCreateView.as_view(), name='create_order'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/archive/', ProductDeleteView.as_view(), name='product_delete'),
    path('orders/<int:pk>/delete/', OrderDeleteView.as_view(), name='order_delete'),
    path('orders/<int:pk>/update/', OrderUpdateView.as_view(), name='order_update'),




]
