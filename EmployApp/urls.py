from django.contrib import admin
from django.urls import path, include
from EmployApp import views

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('<int:id>/', views.Update, name='update'),
    path('about/', views.AboutUS, name='about'),
    path('services/', views.Services, name='services'),
    path('delete/<int:id>/', views.Delete_record, name='delete'),
    path('chatbot/', include('chatbot.urls')), 
]