"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import persona_list, persona_detail, persona_create, persona_update, persona_delete

urlpatterns = [
    path('personas/', persona_list, name='persona_list'),
    path('personas/<int:pk>/', persona_detail, name='persona_detail'),
    path('personas/create/', persona_create, name='persona_create'),
    path('personas/<int:pk>/update/', persona_update, name='persona_update'),
    path('personas/<int:pk>/delete/', persona_delete, name='persona_delete'),
]



