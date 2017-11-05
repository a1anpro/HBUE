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
    current_course = Course.objects.get(id=current_id)#不管是提交了表单还是未提交表单，都需要查询当前这门课
    if request.POST:
        passrate = int(request.POST['passrate'])
        callrate = int(request.POST['callrate'])
        getrate = int(request.POST['getrate'])
        remarkContent = request.POST['remarkContent']
        current_user = request.session['current_user']#得到当前用户
        current_remark = Comment.objects.create(passRate=passrate,callRate=callrate, getRate=getrate,comment=remarkContent,course_id=current_course.id,user_id=current_user.id)
        current_remark.save()
    else:
        print("没有表单提交")#测试

    #查询这个老师的其他课：
    otherCourses = Course.objects.filter(teacher_id=current_course.teacher.id)
    #查询教这门课的其他老师：
    otherTeachers = Course.objects.filter(clss_id=current_course.clss_id)

    thisCourseRemark = Comment.objects.filter(course_id = current_id)#当前课的所有评论

    return render(request,"course.html",
                  {
                    'course':current_course,
                    'otherCourses':otherCourses,
                    'otherTeachers':otherTeachers,
                    'thisCourseRemark':thisCourseRemark,
                    'lastRate_list': [2, 4, 6, 8, 10],
                  })