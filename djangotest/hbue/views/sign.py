
from django.http import HttpResponse


def sin(request):
    return HttpResponse("Sign In")

def sup(request):
    return HttpResponse("Sign Up")

