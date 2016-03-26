from django.conf.urls import url
from django.contrib import admin

from goqual.views import HomeTemplateView
from video.views import VideoDetailView, VideoCreateView, VideoListView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    url(r'^$', HomeTemplateView.as_view(), name="home"),

    url(r'^videos/$', VideoListView.as_view(), name="videos"),
    url(r'^videos/(?P<pk>\d+)/$', VideoDetailView.as_view(), name="video"),
    url(r'^videos/add/$', VideoCreateView.as_view(), name="new_video"),
]
