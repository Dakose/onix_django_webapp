from django.shortcuts import render, redirect
from services.models import UserService
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserChangeForm

def authentication_page(request):
    return render(request, 'authentication/index.html')


def base(request):
    return render(request, 'base.html')

def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your Account has been successful created.")

        return redirect('signin')

    return render(request, 'authentication/signup.html')

def useredit(request):
    form_class = UserChangeForm
    tamplate_name = 'authentication/edit_profile.html'
    success_url = reverse_lazy('home')

    return render(request, 'authentication/edit_profile.html')


def signin(request):

    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "authentication/index.html", {'fname': fname})
        
        else:
            messages.error(request, "Bad Credentials")
            return redirect('signpage')

    return render(request, 'authentication/signin.html')

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('authentication_page')
