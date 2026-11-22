from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookListAPIView.as_view(), name='api-books'),
    path('reviews/', views.ReviewListAPIView.as_view(), name='api-reviews'),
    path('requests/', views.RequestListAPIView.as_view(), name='api-requests'),
]