from django.http import HttpResponse
from django.template import loader


def home(request):
    return HttpResponse("Welcome to the homepage!")


def videos(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
