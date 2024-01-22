from django.shortcuts import render
from .models import BookInstance, Author, Book, Genre
from django.views import generic

def index(request):
    word_books_are_filtered_by = 'foundation'
    num_books = Book.objects.count()
    num_instances = BookInstance.objects.count()
    num_genres = Genre.objects.count()
    num_books_with_word = Book.objects.filter(title__icontains=word_books_are_filtered_by).count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    return render(
        request,
        'index.html',
        context=
        {'num_books': num_books, 'num_instances': num_instances,
         'num_instances_available': num_instances_available, 'num_authors': num_authors,
         'num_genres': num_genres, 'num_books_with_word': num_books_with_word,
         'word': word_books_are_filtered_by, 'num_visits': num_visits}
    )

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10

class AuthorDetailView(generic.DetailView):
    model = Author
