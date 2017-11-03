from django.shortcuts import render
from django.http import Http404, HttpResponse
import string
from hbue.models import *
from hbue.static.function import index

# 个人页面
def user_x(request, userId):
    current_user = User.objects.get(id=userId)
    print('当前用户：',current_user.userInfo)

    return render(request,"user.html",
                  {
                      'current_user':current_user,
                  })

def user_inner(request):
    return HttpResponse("User_Inner")