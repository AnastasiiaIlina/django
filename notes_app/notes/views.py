from django.shortcuts import render
from django.http import HttpResponse

def return_home_page(request):
    notes_list = [
        {
            "title": "My first note!",
            "description": "It`s my first note description...",
            "is_done": False
        },
        {
            "title": "My second note!",
            "description": "It`s my second note description...",
            "is_done": True
        }
    ]

    return render(request, "home_page.html", context={
        "notes_list": notes_list 
    })

