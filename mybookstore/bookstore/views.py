from django.shortcuts import render
from django.views import generic

from .models import Book, Genre
# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request,'index.html', {"books": books})
class BookView(generic.ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'

