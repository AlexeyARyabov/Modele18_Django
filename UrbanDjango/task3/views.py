from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class ManePage(TemplateView):
    template_name = 'third_task/index.html'

def ls_books(request):
    title = "Книги|Каталог"
    books = [
        {"name": "Война и мир", "author": "Л. Толстой"},
        {"name": "Трое из Простоквашино", "author": "Э. Успенский"},
        {"name": "Война миров", "author": "Г. Уэллс"},
    ]
    context = {
        "title": title,
        "books": books,
    }
    return render(request, 'third_task/books.html', context)

class Cart(TemplateView):
    template_name = 'third_task/cart.html'
