from django.contrib import admin
from django.urls import path, include
from . import views
from services.views import HomeView

urlpatterns = [
    path('', views.authentication_page, name="authentication_page"),
    path('home', HomeView.as_view(), name="home"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
]
