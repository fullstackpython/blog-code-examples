from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'(?P<slug>[\wa-z-]+)/', views.they, name="they"),
]
