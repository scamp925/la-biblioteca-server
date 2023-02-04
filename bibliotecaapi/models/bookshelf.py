'''Imports for BookShelf Model'''
from django.db import models
from .book import Book
from .shelf import Shelf
from .user import User

class BookShelf(models.Model):
    '''BookShelf Class'''
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    '''on_delete: When a book is trying to be deleted, a protect error will be triggered; thus, not allowing for the book to be deleted because the book is associated with a shelf. Book can be deleted after all associated shelves are deleted first.'''
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    '''on_delete: When user is deleted, all associated books on user's shelves will also be removed'''
