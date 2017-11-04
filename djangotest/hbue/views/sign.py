from django.shortcuts import render
from django.http import Http404, HttpResponse,HttpResponseRedirect
import string
from hbue.models import *

def signin(request):
    returnInfo=''#如果用户不存在，内容是用户不存在，请注册；如果id存在但是密码不匹配返回，密码错误。
    if request.method != 'POST':
        raise Http404('Only POSTs are allowed')
    else:
        if request.POST['userId'] and request.POST['password']:#都获取到了
            #查询是否有这个id
            ifExist = User.objects.filter(userId=request.POST['userId']).count()
            if int(ifExist)==0:#没有这个人
                returnInfo = '该帐户不存在，请重新登陆'
            else:
                #有这个人，比较密码是否相同
                current_user = User.objects.get(userId=request.POST['userId'])
                if current_user.password == request.POST['password']:
                    #登陆成功，设置session，重定向到主页
                    request.session['hasLogedin'] = True
                    # print('当前用户测试:',current_user)#测试当前用户
                    request.session['current_user'] = current_user#将当前查到的用户对象放到session
                    # print('session对象测试：', request.session['current_user'])
                    # print('hasLogedin测试:', request.session['hasLogedin'])
                    return HttpResponseRedirect('/main')
                else:#没登陆成功跳转到signin.html
                    # print('登陆失败','跳转到signin.html')
                    returnInfo = '密码与学号不匹配，请重新输入密码'
    return render(request,'signin.html',
                  {
                      'returnInfo':returnInfo,
                  })

def signup(request):
    # get 显示注册页面
    # post 显示个人信息页面
    returnInfo=''
    academy = ['信息工程学院','金融学院','经济与环境资源学院','工商管理学院','艺术设计学院','会计学院','法学院','外国语学院','马克思主义学院','体育经济与管理学院']
    if request.POST and request.POST['userId']:#如果POST成功，再进行下一步
        if request.POST['userId'] and request.POST['userName'] and request.POST['pwd1']:
            # print(request.POST['userId'],request.POST['userName'],request.POST['password'], academy[int(request.POST['academy'])])
            sameIdCnt=User.objects.filter(userId=request.POST['userId']).count()#如果为None才写数据，否则重复,返回一句话：已有帐户，请登陆
            # print('相同id的个数:', sameIdCnt)
            # print('用户id:', request.POST['userId'])
            if int(sameIdCnt)!=0:
                returnInfo='该同学已经注册，请登陆或重新注册！'
            else:
                user=User.objects.create(userId=request.POST['userId'],userName=request.POST['userName'],password=request.POST['pwd1'],userAcademy=academy[int(request.POST['academy'])])
                user.save()
                #数据库写成功
                return HttpResponseRedirect('/user/' + str(user.id))#这里应该登陆状态
    # else:
        # returnInfo='未提交成功，请重新提交！'
    return render(request, "signup.html",
                  {
                      'returnInfo':returnInfo,
                  })



def reset(request):
    return HttpResponse("Reset Password")
