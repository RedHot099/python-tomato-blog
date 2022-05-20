from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def papryka(request):
    return render(request, 'pomidory-paprykowe.html')


def czekolada(request):
    return render(request, 'pomidory-czekoladowe.html')


def czarne(request):
    return render(request, 'czarne-pomidory.html')


def tygrysie(request):
    return render(request, 'pomidory-tygrysie.html')