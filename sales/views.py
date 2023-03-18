from django.shortcuts import render 
from django.contrib.auth.decorators import login_required
 

@login_required
def index(request): 
    return render(request, 'sales/vehicle.html',{'title':'Sales','sale':'sale'})
