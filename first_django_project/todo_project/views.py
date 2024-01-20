from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, py!")


def return_simple_html(request):
    data = {
        'authors_list': [
            {
                'name': 'Author 1',
                'books_amount': 2,
                'rating': 4.6
            },
            {
                'name': 'Author 2',
                'books_amount': 4,
                'rating': 2.3
            },
            {
                'name': None,
                'books_amount': 1,
                'rating': 5.0
            }
        ]
    }
    return render(request, 'child.html', context=data)