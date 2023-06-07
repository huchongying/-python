from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

from users.forms import LoginForm
# Create your views here.
from django.shortcuts import render
from django.contrib.auth import authenticate, login

from django.contrib.auth.models import User


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            success_message = '登录成功'  # 登录成功消息
            return render(request, 'user_login.html', {'success_message': success_message})

        error_message = '用户名或密码不正确'  # 登录失败消息
        return render(request, 'user_login.html', {'error_message': error_message})

    return render(request, 'user_login.html')


def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 检查用户名是否已存在
        if User.objects.filter(username=username).exists():
            error_message = '用户名已存在'
            return render(request, 'user_register.html', {'error_message': error_message})

        # 创建用户
        user = User.objects.create_user(username=username, password=password)

        # 登录用户
        login(request, user)

        # 注册成功后的处理，可以重定向到其他页面或显示成功消息
        success_message = '注册成功'
        return render(request, 'user_login.html', {'success_message': success_message})

    return render(request, 'user_register.html')
