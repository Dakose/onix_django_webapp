from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import UserService
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect

class HomeView(ListView):
    model = UserService
    template_name = 'home.html'
    # ordering = ['-id']

    
def service_detail(request, pk):
    service = get_object_or_404(UserService, pk=pk)
    total_likes = service.total_likes()
    liked = False
    if service.likes.filter(id=request.user.id).exists():
        liked = True
    return render(request, 'service_details.html', {'service': service, 'total_likes': total_likes, 'liked': liked})

class AddServiceView(CreateView):
    model = UserService
    fields = '__all__'
    template_name = 'add_service.html'

class UpdateServiceView(UpdateView):
    model = UserService
    fields = '__all__'
    template_name = 'update_service.html'

class DeleteServiceView(DeleteView):
    model = UserService
    template_name = 'delete_service.html'
    success_url = reverse_lazy('home')

def LikeView(request, pk):
    service = get_object_or_404(UserService, id=request.POST.get('service_id'))
    liked = False
    if service.likes.filter(id=request.user.id).exists():
        service.likes.remove(request.user)
        liked = False
    else:
        service.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('service_details', args=[str(pk)]))