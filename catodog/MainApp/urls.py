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
from django.templatetags.static import static
from django.urls import path, include

from catodog import settings
from . import views
from .views import AnimalDetail, TransferDetail, ActDetail

app_name = 'MainApp'

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('createReuest/', CreateRequest.as_view, name='CreateRequest_url')
    path('', views.index, name='index'),
    path('<int:animal_id>/', views.detail, name='detail'),
    path('add_request/', views.add_request, name='add_request'),
    path('check_list/', views.check_list, name='check_list'),
    path('animal_map/', views.animal_map, name='animal_map'),
    path('about/', views.about, name='about'),
    path('news/', views.news, name='news'),
    path('pets/', views.pets, name='pets'),
    # path('act/', views.act, name='act'),
    path('createpets/', views.add_animals, name='add_animals'),
    path('<int:id>', AnimalDetail.as_view(), name='animal_detail'),
    path('request/', views.requests_all, name='request_all'),
    path('catcher/', views.catcher, name='catcher'),
    path('lost/', views.lost_animals, name='lost_animals'),
    # path('act/<int:id>', TransferDetail.as_view(), name='act_detail'),
    path('changestatus/<int:req_id>/<str:stat_id>/', views.changestatus, name='changestatus'),
    # path('act/<int:id>', TransferDetail.as_view(), name='act_detail'),
    path('act/<int:id>', ActDetail.as_view(), name='act_detail')
]
