from django.contrib import admin
from django.urls import path, include
from . import views
from services.views import HomeView, ArticleDetailView
from about.views import about

urlpatterns = [
    path('authentication_page', views.authentication_page, name="authentication_page"),
    path('home', HomeView.as_view(), name="home"),
    path('about', about, name="about"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-details"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
]
