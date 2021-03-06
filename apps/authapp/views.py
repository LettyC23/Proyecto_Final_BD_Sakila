from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import LoginForm, RegistrationForm      

def signin(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect('sakila:buscar_actor')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos!!')

    context = {
        'form': forms
    }
    return render(request, 'signin.html', context)


def signup(request):

    forms = RegistrationForm()
    if request.method == 'POST':
        forms = RegistrationForm(request.POST)
        if forms.is_valid():
            firstname = forms.cleaned_data['firstname']
            lastname = forms.cleaned_data['lastname']
            email = forms.cleaned_data['email']
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            confirm_password = forms.cleaned_data['confirm_password']
            if password == confirm_password:
                try:
                    User.objects.create_user(username=username, password=password, email=email, first_name=firstname, last_name=lastname)

                    return redirect( '/auth/signin')
                except:
                    context = {
                        'form': forms,
                        'error': 'This Username Already exists!'
                    }
                    messages.warning(request, 'Este Usuario ya existe!! Usa otro nombre de usuario')
                    return render(request, 'signup.html', context)
            else:
                messages.warning(request, 'Recuerda, La contraseña debe de coincidir!!')
        else:
            messages.warning(request, 'Recuerda,sólo letras en los campos de nombre y apellido!!')
    context = {
        'form': forms
    }

    return render(request, 'signup.html', context)

def signout(request):
    logout(request)
    return redirect('authapp:signin')