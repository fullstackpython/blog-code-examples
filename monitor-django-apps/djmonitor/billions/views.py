from django.http import HttpResponse
from django.shortcuts import render


def theyare(request):
    return HttpResponse("billions")
