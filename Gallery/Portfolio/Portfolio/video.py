from django.db import models

class Video (models.Model):
    video=models.FileField(upload_to="Images/video")
    caption=models.TextField()