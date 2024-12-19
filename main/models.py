from django.db import models
from django.contrib.auth.models import User

class Sport(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Venue(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=100)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    time = models.TimeField()
    image = models.ImageField(upload_to='events/')

    def __str__(self):
        return f"{self.name} - {self.sport.name}"

class Athlete(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='athletes/', null=True, blank=True)
    biography = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tickets')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.IntegerField()

    def __str__(self):
        return f"{self.event.name} Ticket - ${self.price}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"Booking by {self.user.username} for {self.quantity} tickets."

class Story(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title

