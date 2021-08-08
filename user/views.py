from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username').strip()
        password = request.POST.get('password')
        password_conf = request.POST.get('password_conf')

        if password == password_conf:   
            if User.objects.filter(username=username).exists():
                messages.info(request, "The Username already exists")
                return redirect('/register/')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('/login/')

        else:
            messages.info(request, "The two passwords didn't match")
            return redirect('/register/')

    else:
        return render(request, 'user/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username').strip()
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password) #This is critical
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "You're not a registered User")
            return redirect('/login/')
    else:
        return render(request, "registration/login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')

# Create your views here.
