from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import UserService

# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):
    model = UserService
    template_name = 'home.html'