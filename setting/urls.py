from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.nations, name='nations'),
    path('regions/', views.regs, name='regs'),  
    path('region/', views.region, name='region'),   
    path('zones/', views.zones, name='zons'),
    path('woredas/', views.woredas, name='wored'),
    path('services/', views.services, name='serv'),
    
    path('zone/', views.zone, name='zone'),  
    path('woreda/', views.woreda, name='woreda'),  
    path('insert/', views.insert, name='insert'),  

] 