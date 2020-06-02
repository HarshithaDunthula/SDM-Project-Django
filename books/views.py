from django.views import generic
from .models import Book
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import csv


class IndexView(generic.ListView):
    template_name = 'books/index.html'
    context_object_name = 'all_books'

    def get_queryset(self):
        return Book.objects.all()


class DetailView(generic.DetailView):
    model = Book
    template_name = 'books/details.html'


class BookCreate(CreateView):
    model = Book
    fields = ['_id', 'book_title', 'author', 'book_type', 'reviews_count', 'price', 'rating', 'cover_img']

    def get_success_url(self):
        return reverse_lazy('books:index')


class BookUpdate(UpdateView):
    model = Book
    fields = ['_id', 'book_title', 'author', 'book_type', 'reviews_count', 'price', 'rating', 'cover_img']
    success_url = reverse_lazy('books:index')


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books:index')
