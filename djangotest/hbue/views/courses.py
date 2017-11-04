from django.shortcuts import render

from hbue.models import *


def All(request, current_page="1"):
    courses = Course.objects.all()
    for x in courses:
        x.lastRate = int((x.getRate+x.callRate+x.passRate)/3) + 5
        # print(x.lastRate)
    # print("len:" + str(len(courses)))#长度测试

    return render(request,'courses.html',
                  {'isSearch':False,
                   'courseNum':len(courses),
                   'courses':courses,
                   'lastRate_list':[2,4,6,8,10],
                   })
    # return HttpResponse(courses)
    #return HttpResponse("All " + current_page)

def One(request, current_id):
    current_course = Course.objects.get(id=current_id)
    #查询这个老师的其他课：
    otherCourses = Course.objects.filter(teacher_id=current_course.teacher.id)
    #查询教这门课的其他老师：
    otherTeachers = Course.objects.filter(clss_id=current_course.clss_id)

    return render(request,"course.html",
                  {
                    'course':current_course,
                    'otherCourses':otherCourses,
                    'otherTeachers':otherTeachers,
                  })
    # return HttpResponse("Course " + id)