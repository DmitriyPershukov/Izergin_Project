from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

#admin.site.register(Author)
#admin.site.register(Book)
#admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)

class BookInline(admin.TabularInline):
    model = Book
    extra = 0
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ["first_name", 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]

admin.site.register(Author, AuthorAdmin)

class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    list_filter = ['author']
    inlines = [BookInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'uniqueid')
    list_filter = ("status", "due_back")
    fieldsets = (
        (None, {
            'fields': ('book', 'uniqueid')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )