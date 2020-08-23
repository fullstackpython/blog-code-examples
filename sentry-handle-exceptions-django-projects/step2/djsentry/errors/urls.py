# djsentry/errors/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.errors_index, name="index"),
]
