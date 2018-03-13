# coding=utf-8
# @Time    : 2018/3/5 22:12
# @Author  : XinZhewu_568580410@qq.com

from django.urls import path
from django.contrib.auth.views import login
from . import views


app_name = 'users'
urlpatterns = [
    # 登陆页面
    path('login/', login, {'template_name': 'users/login.html'}, name='login'),

    # 注销
    path('logout/', views.logout_view, name='logout'),

    # 注册
    path('register/', views.register, name='register'),
]
