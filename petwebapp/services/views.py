from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import UserService

class HomeView(ListView):
    model = UserService
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = UserService
    template_name = 'article_details.html'