from django import forms
from .models import Note, User

class NoteForm(forms.ModelForm):
    title = forms.CharField(
        label='Title', 
        max_length=100, 
        widget=forms.TextInput(attrs={ 'class': 'form-control mb-2'})
    )
    description = forms.CharField(
        label='Description',
        widget=forms.TextInput(attrs={ 'class': 'form-control  mb-2'})
    )
    reminder = forms.DateTimeField(
        label='Reminder',
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control mb-2' }),
    )
    category = forms.ChoiceField(
        label='Category', 
        widget=forms.Select(attrs={ 'class': 'form-control mb-2'}),
        choices=(
            ('home', 'home'),
            ('work', 'work'),
            ('health', 'health')
    ))

    class Meta:
        model = Note
        fields = ['title', 'description', 'reminder', 'category']


class LoginForm(forms.ModelForm):
    username = forms.CharField(
        label='Username', 
        max_length=100, 
        widget=forms.TextInput(attrs={ 'class': 'form-control mb-2'})
    )
    password = forms.CharField(
        label='Password', 
        max_length=100, 
        widget=forms.PasswordInput(attrs={ 'class': 'form-control mb-2'})
    )

    class Meta:
        model = User
        fields = ['username', 'password']
