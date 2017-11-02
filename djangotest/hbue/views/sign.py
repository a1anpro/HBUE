
from django.http import HttpResponse


def sin(request):

    # get 显示登陆页面
    # post 显示个人信息页面

    return HttpResponse("Sign In")

def sup(request):

    # get 显示注册页面
    # post 显示个人信息页面

    return HttpResponse("Sign Up")


def reset(request):
    return HttpResponse("Reset Password")
