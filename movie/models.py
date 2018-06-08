from django.db import models
from django.utils import timezone


class Movie(models.Model):
    uploader = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    year = models.CharField(max_length=6)
    file = models.CharField(max_length=600)
    upload_date = models.DateTimeField(blank=True, null=True)

    def upload(self):
        self.upload_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title + "(" + self.year + ")"



