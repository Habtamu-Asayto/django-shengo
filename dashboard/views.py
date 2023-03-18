from django.shortcuts import render 
from django.contrib.auth.decorators import login_required

from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext

@login_required
def index(request):
    trans = translate(language='en')
    return render(request, 'dashboard/index.html',{'title':'Dashboard', 'trans':trans})

def about(request):
    return render(request, 'about.html', {'title':'About'})

def contact(request):
    return render(request, 'contact.html', {'title':'Contact'})


def translate(language):
    cur_language=get_language()
    try:
        activate(language)
        textdashboard = gettext('sidebar-dash') 
        textsetting = gettext('sidebar-setting') 
        textnation = gettext('sidebar-nation') 
        textregion = gettext('sidebar-region') 
        textzone = gettext('sidebar-zone') 
        textworeda = gettext('sidebar-woreda') 
        textservice = gettext('sidebar-service')  
        textCase = gettext('sidebar-type') 
        textprofile = gettext('sidebar-profile') 
        textaccount = gettext('sidebar-account')  
        textlogout = gettext('sidebar-logout')
         

    finally:
        activate(cur_language)
    return (  
             textdashboard,
             textsetting, 
             textnation, 
             textregion, 
             textzone, 
             textworeda,
             textservice,      
             textCase,
             textprofile,
             textaccount,
             textlogout  
            )



 
def charts(request):
    return render(request, 'dashboard/charts.html')


def widgets(request):
    return render(request, 'dashboard/widgets.html')




def tables(request):
    return render(request, "dashboard/tables.html")




def grid(request):
    return render(request, "dashboard/grid.html")




def form_basic(request):
    return render(request, "dashboard/form_basic.html")




def form_wizard(request):
    return render(request, "dashboard/form_wizard.html")




def buttons(request):
    return render(request, "dashboard/buttons.html")




def icon_material(request):
    return render(request, "dashboard/icon-material.html")




def icon_fontawesome(request):
    return render(request, "dashboard/icon-fontawesome.html")




def elements(request):
    return render(request, "dashboard/elements.html")




def gallery(request):
    return render(request, "dashboard/gallery.html")





def invoice(request):
    return render(request, "dashboard/invoice.html")



def chat(request):
    return render(request, "dashboard/chat.html")


