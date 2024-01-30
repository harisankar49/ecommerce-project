from django.urls import path

from . import views
app_name='cart'

urlpatterns = [
    path('cart_detail/', views.cart_detail, name='cart_detail'),
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('remove/<int:product_id>/',views.cart_remove,name='substract_cart'),
    path('full_remove/<int:product_id>/',views.full_remove,name='remove_cart')
]