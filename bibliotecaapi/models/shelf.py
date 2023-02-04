'''Imports for Shelf Model'''

from django.db import models

class Shelf(models.Model):
    '''Shelf Class'''
    label = models.CharField(max_length=50)
