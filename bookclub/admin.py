from django.contrib import admin
from .models import Author, Genre, Book, BookRequest, Review

admin.site.register(Author)
admin.site.register(Genre)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'available')
    list_filter = ('available', 'genre')
    search_fields = ('title', 'author__name')


@admin.register(BookRequest)
class BookRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'status', 'requested_at')
    list_filter = ('status',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'rating', 'created_at')