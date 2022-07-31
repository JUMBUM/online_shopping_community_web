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
    path('admin/', views.admin_main),
    path('admin/store', views.admin_store),
    path('admin/payment/', views.admin_pay),
    path('admin/product/', views.admin_product),
    path('admin/stock/', views.admin_stock),
    path('admin/delivery/', views.admin_delivery),
    path('admin/mem_info/', views.admin_member),      
    path('admin/sel_info/', views.admin_seller), 
    path('admin/post/', views.admin_post), 
    path('admin/notice/', views.admin_notice), 
    path('admin/login/', views.admin_login), 
    path('admin/find_id/', views.admin_find_id),
    path('admin/find_pw/', views.admin_find_pw),
    path('admin/find_pw02/', views.admin_find_pw02),
    path('admin/find_pw03/', views.admin_find_pw03),   
    path('comu_follow/', views.comu_follow),
    path('comu_gal_recent/', views.comu_gal_recent),
    path('comu_gal_best/', views.comu_gal_best),
    path('comu_post_gk1234/', views.comu_post_gk1234),
    path('comu_post_gk1235/', views.comu_post_gk1235),
    path('comu_post_gk1237/', views.comu_post_gk1237),
    path('comu_post_gk1238/', views.comu_post_gk1238),
]
