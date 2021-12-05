from django.urls import path

from greatkart import views
from . import views

urlpatterns = [
    path('', views.store, name= 'store'),
    path('<slug:category_slug>/', views.store, name= 'products_by_category'),
    
] 