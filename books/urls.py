from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    # /books/
    path('', views.IndexView.as_view(), name='index'),

    # /books/<book_id>
    path('<int:pk>/', views.DetailView.as_view(), name='details'),

    # /books/add
    path('book/add/', views.BookCreate.as_view(), name='book-add'),

    # /books/2/
    path('<int:pk>/update/', views.BookUpdate.as_view(), name='book-update'),

    # /books/2/delete/
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book-delete'),
]