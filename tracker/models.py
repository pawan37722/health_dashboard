from django.db import models
from django.contrib.auth.models import User

class HealthEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    weight = models.FloatField()
    sleep_hours = models.FloatField()
    blood_pressure = models.CharField(max_length=20)
    sugar_level = models.FloatField()

    def __str__(self):
        return f"{self.user.username} - {self.date}"

# Create your models here.
