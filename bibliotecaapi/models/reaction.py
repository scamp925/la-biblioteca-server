'''Imports for Reaction Model'''

from django.db import models

class Reaction(models.Model):
    '''Reaction Class'''
    label = models.CharField(max_length=50)
    image_url = models.CharField(max_length=200)

    @property
    def reaction_clicked(self):
        return self.__reaction_clicked
    
    @reaction_clicked.setter
    def reaction_clicked(self, bool):
        self.__reaction_clicked = bool
        
    @property
    def reaction_count(self):
        return self.__reaction_count
    
    @reaction_count.setter
    def reaction_count(self, value):
        self.__reaction_count = value
