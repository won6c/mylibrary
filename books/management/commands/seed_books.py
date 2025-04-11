from django.core.management.base import BaseCommand
from books.models import Book

class Command(BaseCommand):
    help = 'Insert sample books'

    def handle(self, *args, **kargs):
        Book.objects.create(title='1984', author='George Orwell')
        Book.objects.create(title='Brave New World', author="Aldous Huxley")
        Book.objects.create(title="Farhenheit 451", author = "Ray Badbury")
        self.stdout.write(self.style.SUCCESS('Sample books inserted!'))


