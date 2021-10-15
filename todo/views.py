from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout,  login as auth_login
from django.contrib.auth.models import User


from todo import forms


def login(request):
    form = forms.LoginForm(request.POST or None)

    context = {
        'form': form
    }

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is None:
            return render(request, 'login.html', context)
        auth_login(request, user)
        redirect('index')
    print(form)

    return render(request, 'login.html', context)


def register(request):
    form = forms.RegisterUserForm(request.POST or None)
    if form.is_valid():

        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        newUser = User(username=username)
        newUser.set_password(password)

        newUser.save()
        auth_login(request, newUser)

        return redirect('login')

    context = {
        "form": form
    }
    return render(request, 'register.html', context)
