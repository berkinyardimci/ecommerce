from django.urls import path

from greatkart import views
from . import views

urlpatterns = [
    path('', views.store, name= 'store'),
    
] 