from django.core.exceptions import PermissionDenied
from django.shortcuts import render


def they(request, slug):
    if slug and slug == "are":
        return render(request, 'billions.html', {})
    else:
        raise PermissionDenied("Hmm, can't find what you're looking for.")
