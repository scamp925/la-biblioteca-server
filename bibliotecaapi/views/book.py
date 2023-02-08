from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bibliotecaapi.models import Book

class BookView(ViewSet):
    '''The Gallery's Book View'''

    def retrieve(self, request, pk):
        """Handle GET requests from single book
        Returns:
            Response -- JSON serialized book
        """
        try:
            book = Book.objects.get(pk=pk)

            serializer = BookSerializer(book)
            return Response(serializer.data)
        except book.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        """Handle GET requests to get all books

        Returns:
            Response -- JSON serialized list of books
        """
        books = Book.objects.all()
            
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
class BookSerializer(serializers.ModelSerializer):
    '''JSON serializer for books'''
    class Meta:
        model = Book
        fields = ('id', 'title','author', 'cover_image', 'description', 'length', 'first_published', 'book_shelf')
        depth = 1
