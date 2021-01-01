# djtranscribe/caller/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'dial/(\d+)/$', views.dial, name="dial"),
    url(r'record/$', views.record_twiml, name="record-twiml"),
    url(r'get-recording-url/([A-Za-z0-9]+)/$', views.get_recording_url,
        name='recording-url'),
]
