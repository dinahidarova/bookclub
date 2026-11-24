from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from bookclub.models import Book, Review, BookRequest
from .serializers import BookSerializer, ReviewSerializer, RequestSerializer


class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ReviewListAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RequestListAPIView(generics.ListCreateAPIView):
    queryset = BookRequest.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)