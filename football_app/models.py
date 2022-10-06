from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Game(models.Model):
    host_team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='host_set')
    host_score = models.IntegerField()
    guest_team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='guest_set')
    guest_score = models.IntegerField()

    def __str__(self):
        return f"Gospodarz: {self.host_team}, Gość: {self.guest_team} | Wynik: {self.host_score} : {self.guest_score}"
