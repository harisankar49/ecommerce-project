# urls.py
from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.allproductcat, name='allproductcat'),
    path('<slug:c_slug>/', views.allproductcat, name='products_by_category'),
    path('<slug:c_slug>/<slug:p_slug>/', views.prodetails, name='prodcategorydetal'),
]
