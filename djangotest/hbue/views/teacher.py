from django.http import Http404, HttpResponse

def teachCourse(request, teachid):
    return HttpResponse("teachCourse \nTeacherId " + teachid)