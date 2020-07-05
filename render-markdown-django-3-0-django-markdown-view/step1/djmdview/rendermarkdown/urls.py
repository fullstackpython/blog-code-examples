# djmdview/rendermarkdown/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'', views.rendermarkdown_index, name="index"),
]
