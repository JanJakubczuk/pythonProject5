from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.name} {self.surname}"

class Message(models.Model):
    description = models.CharField(max_length=140)
    sender = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='sender_set')
    receiver = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='receiver_set')

    def __str__(self):
        return f"wiadomość od: {self.sender} do {self.receiver} o treści: {self.description}"

