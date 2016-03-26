from django.views.generic import ListView

from video.models import Video


class VideoListView(ListView):

    model = Video
    context_object_name = "videos"
    template_name = "list.html"
