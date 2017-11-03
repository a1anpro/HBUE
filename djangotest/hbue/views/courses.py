from django.shortcuts import render
from django.http import Http404, HttpResponse
import string
from hbue.models import *
from hbue.static.function import index

def All(request, current_page="1"):
    courses = Course.objects.all()
    for x in courses:
        x.lastRate = int((x.getRate+x.callRate+x.passRate)/3) + 5
        print(x.lastRate)
    # print("len:" + str(len(courses)))#长度测试
    # teacher = Course.objects.filter(teacher_id=courses)
    return render(request,'courses.html',
                  {'isSearch':False,
                   'courseNum':len(courses),
                   'courses':courses,
                   })
    # return HttpResponse(courses)
    #return HttpResponse("All " + current_page)

def One(request, current_id):
    course = Course.objects.get(id=current_id)
    # print("搜到的课：", course)
    return render(request,"course.html",
                  {
                    'course':course,
                  })
    # return HttpResponse("Course " + id)