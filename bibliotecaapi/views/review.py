from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from bibliotecaapi.models import Review, Book, User, ReviewReaction, Reaction

class ReviewView(ViewSet):
    '''La Biblioteca's review view'''
    
    def retrieve(self, request, pk):
        """Handle GET requests for single review
        Returns:
            Response -- JSON serialized review
        """
        try:
            review = Review.objects.get(pk=pk)

            serializer = ReviewSerializer(review)
            return Response(serializer.data)
        except Review.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        """Handle GET requests to get all reviews

        Returns:
            Response -- JSON serialized list of reviews
        """
        reviews = Review.objects.all()
        
        reviews_of_book = request.query_params.get('book', None)
        if reviews_of_book is not None:
            reviews = reviews.filter(book_id=reviews_of_book)
        
        for review in reviews:
            find_review_reactions = ReviewReaction.objects.filter(review=review.id)
            associated_reactions = []
            
            for review_reaction_obj in find_review_reactions:
                reaction_dict={}
                try:
                    reaction = Reaction.objects.get(id=review_reaction_obj.reaction_id)
                    reaction_dict['id']=reaction.id
                    reaction_dict['label']=reaction.label
                    reaction_dict['image_url']=reaction.image_url
                    associated_reactions.append(reaction_dict)
                except:
                    pass
                  
            review.associated_reactions = associated_reactions
            
        serializer = ReviewSerializer(reviews, many=True)
        
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized review instance
        """
        
        book = Book.objects.get(pk=request.data['book_id'])
        user = User.objects.get(pk=request.data['user_id'])
        
        review = Review.objects.create(
            star_rating=request.data['star_rating'],
            content=request.data['content'],
            created_on=request.data['created_on'],
            book=book,
            user=user
        )
        
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
      
    def update(self, request, pk):
        """Handle PUT requests for a review

        Returns:
            Response -- Empty body with 204 status code
        """
        
        review = Review.objects.get(pk=pk)
        review.star_rating = request.data['star_rating']
        review.content = request.data['content']
        review.created_on = request.data['created_on']
        
        review.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        review = Review.objects.get(pk=pk)
        review.delete()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    @action(methods=['get'], detail=True)
    def update_shelf(self, request, pk):
        book = Book.objects.get(pk=pk)
        user = request.query_params.get('user', None)
        get_bookshelves = BookShelf.objects.all()
        bookshelf = get_bookshelves.get(book=book, user=user)

        bookshelf.shelf_id = request.data["shelf_id"]
        
        bookshelf.save()
        return Response({'message': "User's book's shelf has been updated"}, status=status.HTTP_204_NO_CONTENT)
    
    @action(methods=['post'], detail=True)
    def add_reaction(self, request, pk):
        """Review request for a user to add a reaction to review"""
        review = Review.objects.get(pk=pk)
        reaction = Reaction.objects.get(pk=request.data["reaction_id"])
        ReviewReaction.objects.create(
            review=review,
            reaction=reaction
        )
        return Response({'message': "User's reaction added"}, status=status.HTTP_201_CREATED)
    
    @action(methods=['delete'], detail=True)
    def remove_reaction(self, request, pk):
        review = Review.objects.get(pk=pk)
        reaction = Reaction.objects.get(pk=request.data["reaction_id"])
        review_reaction = ReviewReaction.objects.get(
            review=review,
            reaction=reaction
        )
        
        review_reaction.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
class ReviewSerializer(serializers.ModelSerializer):
    '''JSON serializer for reviews'''
    class Meta:
        model = Review
        fields = ('id', 'star_rating', 'content', 'created_on', 'book', 'user', 'associated_reactions')
        depth = 1
