from django.db import models
from django.contrib.auth.models import User

class MeterReading(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slno = models.CharField(max_length=50)
    quarterno = models.CharField(max_length=50)
    meterreading = models.FloatField()
    meterimage = models.ImageField(upload_to='meter_images/')
    submit_option = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Meter Reading for {self.user.username}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    staffno = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username}'s profile"