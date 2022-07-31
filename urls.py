"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from . import views

urlpatterns = [
    
    path('mainscrap/', views.view_mainscrap),
    path('storehome/', views.view_store_home),    
    path('hashtag/', views.view_hashtag), 
    path('hashtag2/', views.view_hashtag2), 
    path('mainwriting/', views.view_mw), 
    path('hashtag_main/', views.view_hashtag_main),
    path('category/', views.view_category),
    path('category_gg/', views.view_category_gagu),
    path('category_gj/', views.view_category_gaju),
    path('category_dc/', views.view_category_deco),
    path('category_fb/', views.view_category_fabr),
    path('category_jm/', views.view_category_jomy),
    path('category_jb/', views.view_category_juba),
    path('category_sa/', views.view_category_sang),
    path('category_sn/', views.view_category_suna),
    path('login/', views.login),
    path('find_id/', views.find_id),
    path('comu_follow/', views.comu_follow),
    path('comu_gal_recent/', views.comu_gal_recent),
    path('comu_gal_best/', views.comu_gal_best),
    path('comu_post_gk1234/', views.comu_post_gk1234),
    path('comu_post_gk1235/', views.comu_post_gk1235),
    path('comu_post_gk1237/', views.comu_post_gk1237),
    path('comu_post_gk1238/', views.comu_post_gk1238),
    path('find_pw/', views.find_pw),
    path('find_pw_02/', views.find_pw2),
    path('find_pw_03/', views.find_pw3),
]
