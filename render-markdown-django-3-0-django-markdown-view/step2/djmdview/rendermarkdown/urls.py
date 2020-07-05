# djmdview/rendermarkdown/urls.py
from django.conf.urls import url
from markdown_view import MarkdownView
from . import views

urlpatterns = [
    url(r'', views.rendermarkdown_index, name="index"),
    path('readme/',
         MarkdownView.as_view(file_name='rendermarkdown/README.md'),
         name="readme"),
]
