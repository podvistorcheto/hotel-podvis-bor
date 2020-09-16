from django.db import models
from django.conf import settings

# The Room model


class Room(models.Model):
    ROOM_CATEGORIES = (
        ('TWIN', 'TWIN ROOM'),
        ('DBL', 'DOUBLE ROOM'),
        ('FAM', 'FAMILY ROOM'),
        ('DSUI', 'DELUXE SUITE'),
        ('APT', 'APARTMENT'),
        ('DAPT', 'DELUXE APARTMENT'),
    )
    number = models.IntegerField()
    category = models.CharField(max_length=10, choices=ROOM_CATEGORIES)
    beds = models.IntegerField()
    capacity = models.IntegerField()
    children_capacity = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.number}. {self.category} with {self.beds} beds for {self.capacity} adults and {self.children_capacity} children'


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f'{self.user} booked {self.room} from {self.check_in} adults and {self.check_out} children'