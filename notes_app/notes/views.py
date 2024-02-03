from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Note
from .forms import NoteForm, LoginForm

def return_home_page(request):
    if request.method == 'GET':
        notes_list = Note.objects.all()

        category_from_qs = request.GET.get('category')
        search_by_title_qs = request.GET.get('search')

        if category_from_qs:
            notes_list = notes_list.filter(category = category_from_qs)

        if search_by_title_qs:
            notes_list = notes_list.filter(title__icontains = search_by_title_qs)
    
        return render(request, "home_page.html", context={
            "notes_list": notes_list
        })
    

def return_add_note_page(request):
    if request.method == 'GET':
        form = NoteForm(request.GET)
        return render(request, "add_note_page.html", context={'form': form})
    
    elif request.method == 'POST':
        form = NoteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home_page')
        

def return_one_note_page(request, id):
    if request.method == 'GET':
        note = Note.objects.get(id=id)
        return render(request, "one_note_page.html", context={'note': note})


def return_edit_note_page(request, id):
    note = Note.objects.get(id=id)

    if request.method == 'GET':
        form = NoteForm(instance=note)
        return render(request, "edit_note_page.html", context={'note': note, 'form': form})
    
    elif request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('one_note_page', id=note.id)

        
    return render(request, "edit_note_page.html", context={'note': note, 'form': form})


def return_delete_note_page(request, id):
    note = Note.objects.get(id=id)
    note.delete()

    return redirect('home_page')  

def return_login_page(request):
    if request.method == 'GET':
        form = LoginForm(request.GET)
        return render(request, "registration/login.html", context={'form': form})

        
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

        
    return render(request, "registration/login.html", context={'form': form})


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"



