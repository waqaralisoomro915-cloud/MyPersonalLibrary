from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('books/', views.books, name='books'),
    path('categories/', views.categories, name='categories'),
    path('favourites/', views.favourites, name='favourites'),
    path('arivals/', views.arivals, name='arivals'),
    path('privacy/', views.privacy, name='privacy'),
]
