from django.views.generic import CreateView

from video.models import Video


class VideoCreateView(CreateView):

    model = Video
    fields = [
        'title',
        'content',
        'url',
        'source',
    ]

    template_name = "new_video.html"
