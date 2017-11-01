from django.http import HttpResponse


# 个人页面
def user_x(request):
    return HttpResponse("User_X")

def user_inner(request):
    return HttpResponse("User_Inner")