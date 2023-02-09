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
            
            user = request.query_params.get('user', None)
            
            find_bookshelf = BookShelf.objects.filter(book=book.id, user=user)
            book_shelf = []
            
            for book_shelf_obj in find_bookshelf:
                try:
                    shelf = Shelf.objects.get(id=book_shelf_obj.shelf_id)
                    book_shelf.append(shelf.label)
                except:
                    pass
            
            book.book_shelf = book_shelf

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
        
        user = request.query_params.get('user', None)
        
        for book in books:
            find_bookshelf = BookShelf.objects.filter(book=book.id, user=user)
            book_shelf = []
            
            for book_shelf_obj in find_bookshelf:
                try:
                    shelf = Shelf.objects.get(id=book_shelf_obj.shelf_id)
                    book_shelf.append(shelf.label)
                except:
                    pass
            
            book.book_shelf = book_shelf
            
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    @action(methods=['post'], detail=True)
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
  
    @action(methods=['put'], detail=True)
    def update_shelf(self, request, pk):
        book = Book.objects.get(pk=pk)
        user = request.query_params.get('user', None)
        get_bookshelves = BookShelf.objects.all()
        bookshelf = get_bookshelves.get(book=book, user=user)

        bookshelf.shelf_id = request.data["shelf_id"]
        
        bookshelf.save()
        
        return Response({'message': "User's book's shelf has been updated"}, status=status.HTTP_204_NO_CONTENT)
    
    @action(methods=['delete'], detail=True)
    def remove_from_shelf(self, request, pk):
        book = Book.objects.get(pk=pk)
        shelf = Shelf.objects.get(pk=request.data["shelf_id"])
        user = User.objects.get(pk=request.data["user_id"])
        bookshelf = BookShelf.objects.get(
            book=book,
            shelf=shelf,
            user=user
        )
        bookshelf.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        

class BookSerializer(serializers.ModelSerializer):
    '''JSON serializer for books'''
    class Meta:
        model = Book
        fields = ('id', 'title','author', 'cover_image', 'description', 'length', 'first_published', 'book_shelf')
        depth = 1
