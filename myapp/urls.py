from . import views
from django.urls import path

urlpatterns=[
    path('',views.home,name='home'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('login/',views.login,name='login'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('api/login/', views.login, name='api_login'),
    path('add_manage/', views.add_manage, name='add_manage'),
    path('add/', views.add, name='add'),
    path('dashboard/', views.dashboard, name='dashboard'),
]

