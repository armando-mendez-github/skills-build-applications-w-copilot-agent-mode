
from djongo import models
from django.contrib.auth.models import AbstractUser

# User model for authentication and profiles
class User(AbstractUser):
    email = models.EmailField(unique=True)
    # Add additional fields as needed
    def __str__(self):
        return self.username

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.ArrayReferenceField(
        to=User,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    def __str__(self):
        return self.name


# Activity logging and tracking
class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    duration = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username} - {self.type}"


# Competitive leaderboard
class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.team.name}: {self.points}"


# Personalized workout suggestions
class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)
    def __str__(self):
        return self.name
