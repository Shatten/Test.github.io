"""DjangoTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path
from firstapp import views

urlpatterns = [
    path('', views.index, name='home'),
    re_path(r'^about', views.about),
    re_path(r'^product/(?P<productid>\d+)/', views.product),
    path('user_my/<str:name>/<int:age>/', views.user_my),
    path('user_my/', views.user_my),
    path('contact', views.contact),
    path('temp/', views.temp),
    path('admin/', admin.site.urls),

]
