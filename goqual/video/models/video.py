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
        ('YOUTUBE','YOUTUBE'),
        ('VIMEO','VIMEO'),
    )
    
    source = models.CharField(
        max_length=1,
        choices=SOURCE_CHOICES,
        blank=True,
        null=True,
    )

    def verify_link(self):
        """
        Verify video_url and check if response is 200
        """
        pass

    
