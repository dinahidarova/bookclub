from rest_framework import generics
from .models import Book, Review, BookRequest
from .serializers import BookSerializer, ReviewSerializer, RequestSerializer

class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ReviewListAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class RequestListAPIView(generics.ListCreateAPIView):
    queryset = BookRequest.objects.all()
    serializer_class = RequestSerializer