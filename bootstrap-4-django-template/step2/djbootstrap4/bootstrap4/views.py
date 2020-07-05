from django.shortcuts import render

def bootstrap4_index(request):
    return render(request, 'index.html', {})
