from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ='home'),
    path('api/contact/', views.contact_form, name='contacts_form'),
    path('api/esports/', views.esports_form, name='esports_form')
]