from django.http import HttpResponse
from django.shortcuts import render

from hbue.models import *


# 个人页面
def user_x(request, userId):
    current_user = User.objects.get(id=userId)
    print('user.py:当前用户：',current_user)

    return render(request,"user.html",
                  {
                      'current_user':current_user,
                  })

def user_inner(request):
    return HttpResponse("User_Inner")