from django.contrib import admin
from django.urls import path
from home import views 
from .views import about

urlpatterns = [
    path("", views.index, name='home'),
    path("index.html", views.index, name='index.hmtl'),
    path("about.html", views.about, name='about.html'),
    path("courses.html", views.courses, name='courses.html'),
    path("contact.html", views.contact, name='contact.html'),
    
]