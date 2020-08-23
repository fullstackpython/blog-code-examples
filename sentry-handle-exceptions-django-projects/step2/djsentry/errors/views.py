# djsentry/errors/views.py
from django.shortcuts import render


def errors_index(request):
    division_by_zero = 1 / 0
    return render(request, 'index.html', {})
