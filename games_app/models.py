from django.db import models

class Platform(models.Model):
    name = models.CharField(max_length=256)
    url = models.CharField(max_length=512)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"

class Game(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    rating = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ManyToManyField('Category')

    def __str__(self):
        return f"Name: {self.name} Description: {self.description} Rating: {self.rating} Price: {self.price}"

class Category(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class GameDetails(models.Model):
    cheat_codes = models.CharField(max_length=512)
    finished = models.BooleanField()
    play_time = models.DurationField()
    game = models.OneToOneField(Game, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cheat_codes}, {self.finished}, {self.play_time}"

