from django import forms
from .models import Note, Category

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
    category = forms.ModelChoiceField(
        label='Category', 
        widget=forms.Select(attrs={ 'class': 'form-control mb-2'}),
        queryset=Category.objects.all())

    class Meta:
        model = Note
        fields = ['title', 'description', 'reminder', 'category']
