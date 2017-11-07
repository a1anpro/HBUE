from django.http import HttpResponse
from django.shortcuts import render

from hbue.models import *


# 个人页面
def user_x(request, userId):
    current_user = User.objects.get(id=userId)
    hisAllComments = Comment.objects.filter(user_id=userId)#查询该用户评论的所有课
    return render(request,"user.html",
                  {
                      'current_user':current_user,
                      'hisAllComments':hisAllComments,
                      'numOfComments':len(hisAllComments),
                  })

def user_inner(request):
    return HttpResponse("User_Inner")