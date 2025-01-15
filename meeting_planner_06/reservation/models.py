from django.db import models
from room.models import Room
from users.models import Users
from datetime import time


# Create your models here.
class Reservation(models.Model):
    title = models.CharField(max_length=50)
    user_name = models.ForeignKey(Users, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.TimeField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    comments = models.CharField(max_length=200)


    def __str__(self):
        return f'{self.user_name}'

    