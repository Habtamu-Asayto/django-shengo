from django.urls import path
from . import views 
 
urlpatterns = [
    path('vehicle', views.index, name='sale-vehicle'), 
]