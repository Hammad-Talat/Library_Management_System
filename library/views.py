from rest_framework import viewsets
from .models import Student, Book, Loan ,Author
from .serializers import StudentSerializer, BookSerializer, LoanSerializer ,AuthorSerializer 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.prefetch_related('books').all()
    serializer_class = AuthorSerializer
@api_view(['GET'])
def get_author_by_name(request, name):
    author = get_object_or_404(Author, name__iexact=name)
    serializer = AuthorSerializer(author)
    return Response(serializer.data)
@api_view(['GET'])
def filter_books_by_title(request):
    title = request.GET.get('title', '')
    print("Hereeeeeeeeeeeeee")
    books = Book.objects.all()
    if title:
        books = books.filter(title__icontains=title)

    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def filter_books_by_year(request):
    year = request.GET.get('year', '')
    books = Book.objects.all()
    if year:
        books = books.filter(published_year=year)

    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
