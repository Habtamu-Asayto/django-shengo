from django.shortcuts import render, redirect
from .models import Nation, Reg, Zon, Wored, ServiceDelivery

from django.contrib.auth.decorators import login_required

from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext

def nations(request):
    nations = Nation.objects.all()
    context = {'nations':nations}
    return render(request, 'setting/nationality.html', context)
 
def region(request):
    region = Reg.objects.all()
    nations = Nation.objects.all() 
    return render(request, 'setting/region.html', {'region':region, 'nations':nations})
 
def regs(request):
    nation = request.GET.get('nation')
    #print(nation)
    regs = Reg.objects.filter(nation = nation)
    context = {'regs':regs}
    return render(request, 'setting/partials/region.html', context)


def zones(request):
    zones = Zon.objects.all()
    context = {'zones':zones}
    return render(request, 'setting/zone.html', context)

def woredas(request):
    woredas = Wored.objects.all()
    context = {'woredas':woredas}
    return render(request, 'setting/woreda.html', context)

@login_required
def services(request): 
    trans = translate(language='am')
    services = ServiceDelivery.objects.all()
    nation = Nation.objects.all() 
    reg = Reg.objects.all()
    zon = Zon.objects.all() 
    wored = Wored.objects.all()  
    return render(request, 'setting/service_delivery.html', {'services':services, 'nation':nation, 'reg':reg, 'zon':zon, 'wored':wored, 'trans':trans})


def translate(language):
    cur_language=get_language()
    try:
        activate(language)
        textservicedo= gettext('sidebar-deliveryo')  
        textaddnewservice= gettext('text-addnew-service')  
        textheadername= gettext('textheader-name')  
        textheaderphone= gettext('textheader-phone')  
        textheaderregion= gettext('textheader-region')  
        textheaderzone= gettext('textheader-zone')  
        textheaderworeda= gettext('textheader-woreda')  
        textheaderdesc= gettext('textheader-description')  
        textheaderaction= gettext('textheader-action')  
        textaddservice= gettext('text-add-service')  
        textdeliveryoffice= gettext('text-delivery-service')  
        textselectregion= gettext('text-select-region')  
        textselectzone= gettext('text-select-zone')  
        textselectworeda= gettext('text-select-woreda')  
        textcancel= gettext('text-cancel')  
        textadd= gettext('text-add')   
        

    finally:
        activate(cur_language)
    return (  
             textdeliveryoffice,
             textheaderregion,
             textheaderphone,
             textheadername,
             textheaderzone,
             textheaderworeda,
             textheaderdesc,
             textheaderaction,
             textaddservice,
             textservicedo, 
             textaddnewservice,
             textadd,
             textcancel,
             textselectworeda,
             textselectzone,
             textselectregion,
            )

def zone(request):
    reg = request.GET.get('reg')
    #print(reg)
    zone = Zon.objects.filter(reg = reg)
    context = {'zone':zone}
    return render(request, 'setting/partials/zone.html', context)
 


def woreda(request):
    zon = request.GET.get('zon')
    #print(zon)
    woreda = Wored.objects.filter(zon = zon)
    context = {'woreda':woreda}
    return render(request, 'setting/partials/woreda.html', context)

def insert(request): 
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        description = request.POST.get('description') 
        reg = Reg(id=request.POST['reg']) 
        zon = Zon(id=request.POST['zon']) 
        wored = Wored(id=request.POST['wored']) 
          
        ser = ServiceDelivery(
            name = name, 
            phone = phone,
            description = description, 
            region = reg,
            zone = zon,
            woreda = wored,
        )


        ser.save() 
        return redirect('serv')

 
