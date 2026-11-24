from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('books/<int:pk>/review/', views.add_review, name='add_review'),
    path('books/<int:pk>/request/', views.request_book, name='request_book'),
    path('my-requests/', views.my_requests, name='my_requests'),
    path('profile/', views.profile, name='profile'),

    # Аутентификация
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]