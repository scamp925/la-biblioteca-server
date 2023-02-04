'''Imports for Review Model'''

from django.db import models
from .book import Book
from .user import User

class Review(models.Model):
    '''Review Class'''
    star_rating = models.IntegerField()
    content = models.TextField()
    created_on = models.DateField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
