from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'home/pages/index.html')


def about(request):
    return render(request, 'home/pages/about.html')


def contact(request):
    return render(request, 'home/pages/contact.html')
