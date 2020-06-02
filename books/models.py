from django.db import models
from django.urls import reverse


class Book(models.Model):
    _id = models.IntegerField()
    book_title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    book_type = models.CharField(max_length=200)
    reviews_count = models.IntegerField()
    price = models.CharField(max_length=200)
    rating = models.CharField(max_length=200)
    cover_img = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse('book:index', kwargs={'pk': self.pk})

    def __str__(self):
        return self.book_title + ' by ' + self.author
