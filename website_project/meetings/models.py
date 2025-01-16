from django.db import models
from django.contrib.auth.models import User

class Meeting(models.Model):
    title = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    meeting_date = models.DateField()
    start_time = models.TimeField()
    duration = models.DurationField()
    meeting_room = models.CharField(max_length=100)
    comments = models.TextField()

    def __str__(self):
        return self.title