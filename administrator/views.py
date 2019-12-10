from django.shortcuts import render
from .forms import NoticeForm


# Create your views here.
def index(request):
    return render(request, 'administrator/pages/index.html')


def login(request):
    return render(request, 'administrator/pages/login.html')


def form_notice(request):
    if request.method == "POST":
        form = NoticeForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = NoticeForm()
    return render(request, 'administrator/pages/form_notice.html', {'form': form})


def form_dues_stu(request):
    return render(request, 'administrator/pages/form_dues_stu.html')


def form_dues_tea(request):
    return render(request, 'administrator/pages/form_dues_tea.html')


def form_hos(request):
    return render(request, 'administrator/pages/form_hos.html')


def form_stu(request):
    return render(request, 'administrator/pages/form_stu.html')


def form_tea(request):
    return render(request, 'administrator/pages/form_tea.html')
