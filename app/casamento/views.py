from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(
        request,
        'casamento/index.html'
    )


def place(request):
    return render(
        request,
        'casamento/local.html'
    )


