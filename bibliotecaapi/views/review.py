from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bibliotecaapi.models import Review, Book, User

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
        
        
        reviews_of_user = request.query_params.get('user', None)
        if reviews_of_user is not None:
            reviews = reviews.filter(customer_id=reviews_of_user)
            
        serializer = ReviewSerializer(reviews, many=True)
        
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized review instance
        """
        
        book = Book.objects.get(pk=request.data['book_id'])
        user = User.objects.get(pk=request.data['customer_id'])
        
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
        
class ReviewSerializer(serializers.ModelSerializer):
    '''JSON serializer for reviews'''
    class Meta:
        model = Review
        fields = ('id', 'star_rating', 'content', 'created_on', 'book', 'user', 'associated_reactions')
        depth = 1
