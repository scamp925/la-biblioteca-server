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
    
    @property
    def associated_reactions(self):
        return self.__associated_reactions
    
    @associated_reactions.setter
    def associated_reactions(self, value):
        self.__associated_reactions = value

    # @property
    # def reaction_clicked(self):
    #     return self.__reaction_clicked
    
    # @reaction_clicked.setter
    # def reaction_clicked(self, bool):
    #     self.__reaction_clicked = bool
        
    # @property
    # def reaction_count(self):
    #     return self.__reaction_count
    
    # @reaction_count.setter
    # def reaction_count(self, value):
    #     self.__reaction_count = value
