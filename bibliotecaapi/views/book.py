from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from bibliotecaapi.models import Book, Shelf, User, BookShelf

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
    
    @action(methods=['put'], detail=True)
    def add_to_shelf(self, request, pk):
      """Book request for a user to add book to a shelf"""

      book = Book.objects.get(pk=pk)
      shelf = Shelf.objects.get(pk=request.data["shelf_id"])
      user = User.objects.get(pk=request.data["user_id"])
      BookShelf.objects.create(
          book=book,
          shelf=shelf,
          user=user
      )
      return Response({'message': "User's book added"}, status=status.HTTP_201_CREATED)
    
class BookSerializer(serializers.ModelSerializer):
    '''JSON serializer for books'''
    class Meta:
        model = Book
        fields = ('id', 'title','author', 'cover_image', 'description', 'length', 'first_published', 'book_shelf')
        depth = 1
