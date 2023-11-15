from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(
        max_length=128,
        erbose_name='Book's Genre',
        help_text='Enter book's genre, like science,fiction,non-fiction'
        )
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='book title',
        help_text='books' title
    )
    author = models.CharField(max_length=128)
    summary = models.TextField(max_length=1000,help_text='the summary of the book')
    isbn = models.CharField('ISBN', max_length=13, help_text="the book\'s ISBN, <a href='https://www.isbn-international.org/content/what-is-isbn'>what is ISBN</a>")
    genre = models.ForeignKey('Genre', help_text='book genre')
    published_at = models.DateField()

    def __str__(self):
        return self.author + ' - ' + self.title