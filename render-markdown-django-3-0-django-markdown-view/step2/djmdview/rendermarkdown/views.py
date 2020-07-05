from django.shortcuts import render


def rendermarkdown_index(request):
    return render(request, 'index.html', {})
