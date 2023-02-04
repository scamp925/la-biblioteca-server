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
    shelf = models.ForeignKey(Shelf, on_delete=models.PROTECT)
    '''on_deleted for shelf: When a shelf is trying to be deleted, a protect error will be triggered; thus, not allowing for the shelf to be deleted because the shelf is associated with a book. Shelf can be deleted after all associated books are deleted first.'''
