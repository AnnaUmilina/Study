from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'authorization/home.html')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'authorization/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currentauthorization')
            except IntegrityError:
                return render(request, 'authorization/signupuser.html', {
                    'form': UserCreationForm(),
                    'error': 'Такое имя пользователя уже существует'})
        else:
            return render(request, 'authorization/signupuser.html', {
                'form': UserCreationForm(),
                'error': 'Пароли не совпадают'
            })


@login_required
def currentauthorization(request):
    return render(request, 'authorization/currentauthorization.html')


@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'authorization/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'authorization/loginuser.html', {
                'form': AuthenticationForm(),
                'error': 'Неверные данные для входа'})
        else:
            login(request, user)
            return redirect('currentauthorization')
