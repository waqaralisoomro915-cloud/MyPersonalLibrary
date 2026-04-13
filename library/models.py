from django.db import models

# Create your models here.
from django.db import models



class Contact(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)  # use CharField for phone numbers
    subject = models.CharField(max_length=100, default='No subject provided')
    message = models.TextField(default='No message provided')

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class requestbook(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.title} {self.author}"

class favourite_books_update(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    image = models.URLField()
    about = models.TextField()
    opnion = models.TextField()
    def __str__(self):
        return f"{self.title} {self.author}"


class ArivalBooks(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField()