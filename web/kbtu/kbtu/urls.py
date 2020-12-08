"""kbtu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from pizza import views
from pizza import api_views
from django.conf.urls.static import static
from kbtu import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('papers/', views.papers),
    path('cars/<int:id>', views.car_view),
    path('cars/<int:id>/delete', views.car_delete),
    path('cars/', views.cars_view),
    path('add_random/', views.cars_add_random),
    path('add/', views.cars_add),
    path('login.html', views.login),
    path('tables.html', views.tables),
    path('cars_img.html', views.cars_img),
    path('', views.index),
    path('index.html', views.index),
    path('api/numbers', api_views.numbers),
    path('api/cars', api_views.cars),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

