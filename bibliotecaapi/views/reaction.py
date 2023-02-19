from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bibliotecaapi.models import Reaction, ReviewReaction

class ReactionView(ViewSet):
    '''La Biblioteca's Reaction View'''
        
    def list(self, request):
        """Handle GET requests to get all reactions

        Returns:
            Response -- JSON serialized list of reactions
        """
        reactions = Reaction.objects.all()
        
        review_id = request.query_params.get('review', None)
        
        for reaction in reactions:
            reaction.reaction_clicked = len(ReviewReaction.objects.filter(review_id = review_id, reaction_id = reaction.id)) > 0
            reaction.reaction_count = len(ReviewReaction.objects.filter(review_id = review_id, reaction_id = reaction.id))
        
        serializer = ReactionSerializer(reactions, many=True)
        return Response(serializer.data)
      
class ReactionSerializer(serializers.ModelSerializer):
    """JSON serializer for reactions"""
    class Meta:
        model = Reaction
        fields = ("id", "label", "image_url", "reaction_clicked", "reaction_count")
        