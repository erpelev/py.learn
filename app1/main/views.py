from lib2to3.fixes.fix_input import context

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context: dict[str, str] = {
        'title': 'Home',
        'content': 'Главная страница магазина - HOME',
        'list': ['first', 'second'],
        'dict': {'first':1},
        'bool': True
    }
    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse('About page')
# Create your views here.
