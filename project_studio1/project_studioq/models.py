from django.db import models

# Create your models here.
def __str__(self):
    return self.name

class Contact(models.Model):
    full_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=10)
    message = models.CharField(max_length=200)

    
    def __str__(self):
        return self.full_name

class Esports(models.Model):
    title = models.CharField(max_length=20)
    duration = models.CharField(max_length=50)
    fee = models.CharField(max_length=20)
    date = models.DateField()
    team_size = models.CharField(max_length=10)
    prize_pool = models.CharField(max_length=20)

    
    def __str__(self):
        return self.title