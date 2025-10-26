from django.db import models

class LearningJourney(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    bio = models.TextField()

    def __str__(self):
        return self.name
