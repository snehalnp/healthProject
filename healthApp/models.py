import uuid
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class MyModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

class HealthRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.FloatField()
    blood_pressure = models.CharField(max_length=20)
    heart_rate = models.IntegerField()
    steps = models.IntegerField()
    sleep_hours = models.FloatField()

    def __str__(self):
        return f"{self.user.username} - {self.date}"



class Food(models.Model):
    name = models.CharField(max_length=100)
    calories = models.IntegerField()

    def __str__(self):
        return self.name

class CalorieIntake(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.date}"



class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.FloatField(help_text='Duration in minutes')

    def __str__(self):
        return f"{self.user.username} - {self.date}"


