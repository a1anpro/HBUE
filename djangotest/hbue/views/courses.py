from django.shortcuts import render
from django.http import Http404, HttpResponse
import string

from hbue.static.function import index

def All(request, current_page="1"):
    return HttpResponse("All " + current_page)

def One(request, id):
    return HttpResponse("Course " + id)