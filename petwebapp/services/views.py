from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import UserService

class HomeView(ListView):
    model = UserService
    template_name = 'home.html'

# class ArticleDetailView(DetailView):
#     model = UserService
#     template_name = 'article_details.html'
    
def service_detail(request, pk):
    service = get_object_or_404(UserService, pk=pk)
    return render(request, 'service_details.html', {'service': service})