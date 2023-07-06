"""
URL configuration for crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.inicio, name="inicio"),
    path('proyecto',views.proyectos),
    path('contactos',views.Contactos),
    path('subirproyec',views.subirprojec),
    path('inicioDeSesion',views.inicioDeSesion),
    path('registro',views.registro),
    path('carrito',views.carrito),
   
]
