from django.db import models


class Dream(models.Model):
    RATE_CHOICES = (
        (1, 'Ok'),
        (2, 'Fine'),
        (3, 'Good'),
        (4, 'Amazing'),
        (5, 'Incredible')
    )

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    time_to_complete = models.CharField(max_length=50)
    wish_rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES, null=True)

    def __str__(self):
        return f'Мечта: {self.name} ID:{self.pk}'

