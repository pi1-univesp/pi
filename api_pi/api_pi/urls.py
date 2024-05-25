"""
URL configuration for api_pi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login),
    path('home/', views.home, name='home'),
    path('listar-medicamentos/', views.listar_medicamentos, name='listar_medicamentos'),
    path('cadastro-de-medicamentos/', views.cadastro_de_medicamentos, name='cadastro_de_medicamentos'),
    path('cadastro-de-novos-usuarios/', views.cadastro_de_novos_usuarios, name='cadastro_de_novos_usuarios'),
    path('sair/', views.sair, name='sair'),
]
