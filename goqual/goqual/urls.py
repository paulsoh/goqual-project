from django.conf.urls import url
from django.contrib import admin

from video.views import VideoDetailView, VideoCreateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^video/(?P<pk>\d+)/$', VideoDetailView.as_view(), name="video"),
    url(r'^video/add/$', VideoCreateView.as_view(), name="new_video"),
]
