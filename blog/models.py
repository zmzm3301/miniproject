from django.db import models


class Post(models.Model):
    battery = models.CharField(max_length=10)
    led_color = models.CharField(max_length=10)
    run_time = models.CharField(max_length=10)

    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'[{self.pk}]{self.battery}, {self.led_color}, {self.run_time}'
