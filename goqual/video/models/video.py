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
    
    source_id = models.CharField(
        max_length=20,
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
    
    def save(self, *args, **kwargs):
        self.source_id = self.get_source_id()
        super(Video, self).save(*args, **kwargs)

    def get_source_id(self):
        """
        Get video id from original source
        Currently only implemented for youtube
        """
        import re
        reg_exp = "^.*(youtu\.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=)([^#\&\?]*).*"
        match = re.search(reg_exp, self.url)
        return match.group(2)

    def verify_link(self):
        """
        Verify video_url and check if response is 200
        """
        pass

    
