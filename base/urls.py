
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('service/<slug:slug>', views.service_detail, name='service_detail'),
    path('blogs', views.blog, name='blogs'),
    path('blog/<slug:slug>', views.blog_detail, name='blog_detail'),
    path('contact', views.contact, name='contact'),
]