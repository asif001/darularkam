from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'notice/pages/index.html')


def notice_details(request):
    return render(request, 'notice/pages/notice_details.html')
