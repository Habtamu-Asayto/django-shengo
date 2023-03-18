from django.shortcuts import render, redirect 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext

def register(request): 
    trans = translate(language='am')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"{username} Your account are created successfully, Login now !")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form, 'trans':trans} )


def translate(language):
    cur_language=get_language()
    try:
        activate(language)
        textTitle = gettext('title') 
        textWelcome = gettext('welcome') 
        textNavHome = gettext('home-nav') 
        textNavAbout = gettext('about-nave') 
        textNavLogin = gettext('login-nav') 
        textNavRegister = gettext('register-nav') 
        textNavProfile = gettext('profile-nav') 
        textNavContact = gettext('contact-nav') 
        textLanguage = gettext('language') 
        textLout = gettext('log-out') 
        textHaveA = gettext('Have-A') 
        textsignHere = gettext('sign-Here') 
        textpwdReset = gettext('pwd-Reset')  
        textSign = gettext('sign')  
        textAlready = gettext('already-have')  
        textsidebarsales = gettext('sidebar-sales') 
        textsidebargifts = gettext('sidebar-gifts')   

    finally:
        activate(cur_language)
    return (textTitle,
             textWelcome, 
             textNavHome, 
             textNavAbout, 
             textNavLogin, 
             textNavProfile,
            textNavRegister, 
            textNavContact, 
            textLanguage, 
            textNavLogin,  
            textLout,
            textHaveA,
            textsignHere,
            textpwdReset, 
            textSign,
            textAlready,  
            textsidebarsales,  
            textsidebargifts,      
            )


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your account has updated successfully !")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)
    context = {
        'u_form': u_form,
        'p_form' : p_form
    }
    return render(request, 'users/profile.html', context)
