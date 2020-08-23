# djsentry/errors/views.py
from django.shortcuts import render


def errors_index(request):
    return render(request, 'index.html', {})
