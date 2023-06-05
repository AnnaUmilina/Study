from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/signupuser.html', {'form': UserCreationForm()})
    else:
        request.POST['password1'] == request.POST['password2']


def currenttodos(request):
    return render(request, 'todo/currenttodos.html')
