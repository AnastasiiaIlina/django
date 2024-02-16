from django import forms
from django.contrib.auth.models import User

from .models import Note, Category

class NoteForm(forms.ModelForm):
    title = forms.CharField(
        label='Title', 
        max_length=100, 
        widget=forms.TextInput()
    )
    description = forms.CharField(
        label='Description',
        widget=forms.TextInput()
    )
    reminder = forms.DateTimeField(
        label='Reminder',
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local' }),
    )
    category = forms.ModelChoiceField(
        label='Category', 
        widget=forms.Select(),
        queryset=Category.objects.all())

    class Meta:
        model = Note
        fields = ['title', 'description', 'reminder', 'category']


class LoginForm(forms.ModelForm):        
    username = forms.CharField(
        label='Username', 
        max_length=100, 
        widget=forms.TextInput()
    )
    password = forms.CharField(
        label='Password', 
        max_length=100, 
        widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = ['username', 'password']