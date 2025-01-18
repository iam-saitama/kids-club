from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('classes/', views.school_classes, name='classes'),
    path('contact/', views.contact, name='contact'),
]
