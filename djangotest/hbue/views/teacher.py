from django.shortcuts import render
from django.http import Http404, HttpResponse
from hbue.models import *

def teachCourse(request, teacherId):
    teacherCourses = Course.objects.filter(teacher_id=teacherId)
    current_teacher = Teacher.objects.get(id=teacherId)

    print(current_teacher.teacherInfo)

    return render(request, "teacher.html", {
        'len': len(teacherCourses),
        'teacherCourses': teacherCourses,
        'current_teacher':current_teacher,
    })
