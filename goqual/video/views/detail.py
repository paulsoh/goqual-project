from django.views.generic import DetailView

from video.models import Video


class VideoDetailView(DetailView):

    model = Video
    template_name = "detail.html"
