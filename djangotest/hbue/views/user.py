from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from hbue.forms import FileUploadForm#对应的表单类
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

def edit(request,userId):
    current_user = User.objects.get(id=userId)
    if request.POST:
        icon = FileUploadForm(request.POST, request.FILES)
        print('icon测试:', icon)
        if icon.is_valid():
            f = icon.cleaned_data['icon']
            # if file != None:
            print('file测试:', f)
            f.name = current_user.userId + f.name[-4:]
            current_user.userIcon = f

        userinfo = request.POST['userInfo']
        current_user.userInfo = userinfo
        current_user.save()
        return HttpResponseRedirect('/user/'+str(current_user.id))
    icon = FileUploadForm()

    return render(request, 'edit.html',
                  {
                      "current_user":current_user,
                      'form': icon
                  })