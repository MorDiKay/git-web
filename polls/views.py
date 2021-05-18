from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.utils.html import format_html


def index(request):
    tit = 'Это другой заголовок'
    return render(request, 'index.html', {'tit': tit})


def change_color(request):
    color = request.GET.get("color", "")
    return render(request, 'index.html', {"color": color})
