from django.contrib import admin
from django.urls import path, include
from . import views
from services.views import HomeView, service_detail, AddServiceView
from about.views import about

urlpatterns = [
    path('authentication_page', views.authentication_page, name="authentication_page"),
    path('home', HomeView.as_view(), name="home"),
    path('about', about, name="about"),
    path('service/<int:pk>/', service_detail, name="service_details"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('add_service/', AddServiceView.as_view(), name="add_service"),
]
