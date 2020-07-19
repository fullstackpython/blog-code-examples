# djmdview/rendermarkdown/urls.py
from django.conf.urls import url
from django.urls import path

from markdown_view.views import MarkdownView
from . import views


urlpatterns = [
    path('readme/',
         MarkdownView.as_view(file_name='rendermarkdown/README.md'),
         name="readme"),
    url(r'', views.rendermarkdown_index, name="index"),
]
