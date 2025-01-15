from django.db import models

# Create your models here.

# Create your models here.
class Room(models.Models):
    room_name = models.CharField(max_length=50)
    floor_number = models.IntegerField()  
    room_number = models.IntegerField()
    

    def __str__(self):
        return f'{self.user_name}'

