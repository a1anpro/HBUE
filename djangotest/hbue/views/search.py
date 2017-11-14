from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from hbue.models import *

def search(request):
    # if 'search' in request.GET and request.GET['search']:
    content = request.GET['search']
    #先查课程名，如果没查到再查老师

    courses = Course.objects.filter(clss__className__icontains=content)
    if courses.count() == 0:
        #search nothing
        courses = Course.objects.filter(teacher__teacherName__icontains=content)

    return render(request, 'courses.html',
                  {
                   'content':content,
                   'isSearch': True,
                   'courseNum': len(courses),
                   'courses': courses,
                   'lastRate_list': [2, 4, 6, 8, 10],
                   })
