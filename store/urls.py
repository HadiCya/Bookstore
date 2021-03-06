from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.all_products, name='all products'),
    path('books/<slug:slug>', views.product_detail, name='product_detail'),
    path('/searchbar', views.searchbar, name='searchbar'),
]