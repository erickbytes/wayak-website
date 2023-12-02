from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. What dates are you traveling?")
