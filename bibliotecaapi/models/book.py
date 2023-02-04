'''Imports for Book Model'''

from django.db import models
from .shelf import Shelf

class Book(models.Model):
    '''Book Class'''
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    cover_image = models.CharField(max_length=100)
    description = models.TextField()
    length = models.IntegerField()
    first_published = models.DateField()
    
    @property
    def book_shelf(self):
        return self.__book_shelf
    
    @book_shelf.setter
    def book_shelf(self, value):
        self.__book_shelf = value
