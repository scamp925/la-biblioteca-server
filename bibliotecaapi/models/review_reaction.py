'''Imports for ReviewReaction Model'''
from django.db import models
from .review import Review
from .reaction import Reaction
from .user import User

class ReviewReaction(models.Model):
    '''ReviewReaction Class'''
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    reaction = models.ForeignKey(Reaction, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
