#登出处理函数:
from django.shortcuts import render
from django.http import Http404, HttpResponse,HttpResponseRedirect
import string
from hbue.models import *

def logout(request):
    #删除当前session中的对象和变量
    del request.session['current_user']
    del request.session['hasLogedin']
    #重定向到主页
    return HttpResponseRedirect('/main')