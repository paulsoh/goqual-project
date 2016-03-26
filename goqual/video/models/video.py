from django.db import models


class Video(models.Model):

    title = models.CharField(
        max_length=80,
    )

    content = models.TextField()

    url = models.URLField(
        blank=True,
        null=True,
    )

    thumbnail = models.ImageField(
        blank=True,
        null=True,
    )

    SOURCE_CHOICES = (
        ('YOUTUBE', 'YOUTUBE'),
        ('VIMEO', 'VIMEO'),
    )

    source = models.CharField(
        max_length=7,
        choices=SOURCE_CHOICES,
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.title

    def verify_link(self):
        """
        Verify video_url and check if response is 200
        """
        pass

    def get_absolute_url(self):
        return reverse(
            "video",
            kwargs={
                "pk": self.id,
            }
        )
