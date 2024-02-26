from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView
from .models import UserService

class HomeView(ListView):
    model = UserService
    template_name = 'home.html'

    
def service_detail(request, pk):
    service = get_object_or_404(UserService, pk=pk)
    return render(request, 'service_details.html', {'service': service})

class AddServiceView(CreateView):
    model = UserService
    fields = '__all__'
    template_name = 'add_service.html'