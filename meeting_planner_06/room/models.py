from django.db import models

# Create your models here.

# Create your models here.
class Room(models.Model):
    room_name = models.CharField(max_length=120)
    floor_number = models.IntegerField()  
    room_number = models.IntegerField()
    def __str__(self):
        return f'{self.room_name}: room {self.room_num} on flooor {self.floor_num}'

