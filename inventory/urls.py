from django.urls import path
from . import views

app_name = "inventory"

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:slug>/', views.category_items, name='category_items'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
]
