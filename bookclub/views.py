from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Avg
from .models import Book, Author, Genre, BookRequest, Review
from .forms import ReviewForm


def home(request):
    books = Book.objects.filter(available=True)[:6]
    return render(request, 'bookclub/home.html', {'books': books})


def book_list(request):
    books = Book.objects.filter(available=True)
    genre_id = request.GET.get('genre')
    search = request.GET.get('search')
    if genre_id:
        books = books.filter(genre__id=genre_id)
    if search:
        books = books.filter(title__icontains=search)
    genres = Genre.objects.all()
    return render(request, 'bookclub/book_list.html', {
        'books': books, 'genres': genres, 'selected_genre': genre_id, 'search': search or ''
    })


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    reviews = book.reviews.select_related('user').all()
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
    user_review = None
    if request.user.is_authenticated:
        user_review = reviews.filter(user=request.user).first()

    form = None
    if request.user.is_authenticated and not user_review:
        form = ReviewForm()

    return render(request, 'bookclub/book_detail.html', {
        'book': book, 'reviews': reviews, 'avg_rating': round(avg_rating, 1),
        'form': form, 'user_review': user_review,
    })


@login_required
def add_review(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if Review.objects.filter(user=request.user, book=book).exists():
        messages.warning(request, "Вы уже оставили отзыв на эту книгу.")
        return redirect('book_detail', pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.book = book
            review.save()
            messages.success(request, "Спасибо за отзыв!")
    return redirect('book_detail', pk=pk)


@login_required
def request_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if BookRequest.objects.filter(user=request.user, book=book, status__in=['pending', 'approved']).exists():
        messages.warning(request, "У вас уже есть активная заявка на эту книгу.")
        return redirect('book_detail', pk=pk)
    BookRequest.objects.create(user=request.user, book=book)
    messages.success(request, f"Заявка на «{book.title}» отправлена!")
    return redirect('my_requests')


@login_required
def my_requests(request):
    requests_list = BookRequest.objects.filter(user=request.user).select_related('book')
    return render(request, 'bookclub/my_requests.html', {'requests': requests_list})


@login_required
def profile(request):
    reviews = Review.objects.filter(user=request.user).select_related('book')
    requests_list = BookRequest.objects.filter(user=request.user).select_related('book')[:5]
    return render(request, 'bookclub/profile.html', {
        'reviews': reviews, 'requests': requests_list,
    })