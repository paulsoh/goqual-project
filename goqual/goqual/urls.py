from django.conf.urls import url
from django.contrib import admin

from video.views import VideoDetailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^video/(?P<pk>\d+)/$', VideoDetailView.as_view(), name="video"), 
]
