from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('classes/', views.schedule_view, name='schedule'),
    path('contact/', views.contact, name='contact'),
]
