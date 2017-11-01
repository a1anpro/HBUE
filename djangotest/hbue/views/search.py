from django.shortcuts import render
from django.http import HttpResponse


def Search(request, cOrt="", current_page="1"):
    return HttpResponse("Search " + cOrt + "'s " + current_page)