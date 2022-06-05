import email
import re
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Gender(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Relation_Type(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=30)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=30)
    genre = models.ManyToManyField('Genre',related_name='genres')
    author = models.ManyToManyField('Author', related_name='authors')

    def __str__(self):
        return self.title

class Reader(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, null=False, blank=False)
    about = models.CharField(max_length=100, null=False, blank=False)
    avatar = models.ImageField(null=True, default='avatar.svg')
    email = models.EmailField(unique=True, null=True)
    popularity = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    books = models.ManyToManyField('Book', related_name='books')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Interested_Gender(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE, null=True, blank=True)
    gender = models.ManyToManyField('Gender', related_name='gender')

    def __str__(self):
        return self.reader.__str__() + 'on ' + self.gender.__str__()

class Interested_Relation(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE, null=True, blank=True)
    relation_type = models.ForeignKey(Relation_Type, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.reader.__str__() + 'on ' + self.relation_type.__str__()

class Grade(models.Model):
    given_by = models.ForeignKey(Reader, on_delete=models.CASCADE, null=False, blank=False, related_name='given_by')
    recieved_by = models.ForeignKey(Reader, on_delete=models.CASCADE, null=False, blank=False, related_name='recieved_by')
    grade = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    block = models.BooleanField()

    def __str__(self):
        return self.given_by.__str__() + ' on ' + self.recieved_by.__str__()
