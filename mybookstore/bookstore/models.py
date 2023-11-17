from django.db import models
from django.utils.timezone import now
# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    date_of_birth = models.DateField(null= True)
    date_of_death = models.DateField(null= True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Genre(models.Model):
    name = models.CharField(
        max_length=128,
        verbose_name="Book's Genre",
        help_text="Enter book's genre, like science,fiction,non-fiction"
        )
    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='book title',
        help_text="books' title"
    )
    author = models.ForeignKey(Author, on_delete= models.CASCADE)
    summary = models.TextField(max_length=1000,help_text='the summary of the book')
    isbn = models.CharField('ISBN', max_length=13, help_text="the book\'s ISBN, <a href='https://www.isbn-international.org/content/what-is-isbn'>what is ISBN</a>")
    genre = models.ManyToManyField(Genre, help_text='book genre')
    published_at = models.DateField(default=now())

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return f'Book: {self.title} published at {self.published_at}'
    