from django.contrib import admin
from django.urls import path
from accounts import views

admin.site.site_header =  "Login to Developer Sarath"
admin.site.site_title =  "Welcome to Sarath's Dashboard"
admin.site.index_title = "Welcome to this portal"



urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('projects/', views.projects, name="projects"),
    path('contact/', views.contact, name="contact"),
]    