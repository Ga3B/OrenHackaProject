"""catodog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from . import views

app_name = 'MainApp'
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('createReuest/', CreateRequest.as_view, name='CreateRequest_url')
    path('', views.index, name='index'),
    path('<int:animal_id>/', views.detail, name='detail'),
    path('add_request/', views.add_request, name='add_request'),
    path('check_list/', views.check_list, name='check_list'),
    path('about/', views.about, name='about'),
    path('news/', views.news, name='news'),
    path('pets/', views.pets, name='pets'),
    path('act/', views.act, name='act')

]
