from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from django.conf import settings

from users import views

app_name='users'
urlpatterns = [
    path('login/', views.user_login,name='login'),  # 登录
    path('register/', views.user_register ,name='register'),  # 注册

]