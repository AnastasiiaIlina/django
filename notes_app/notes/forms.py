from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    title = forms.CharField(label='Title', max_length=100)
    description = forms.CharField(label='Description')
    reminder = forms.DateTimeField(
        label='Reminder',
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
    )
    category = forms.ChoiceField(label='Category', choices=(
        ('home', 'home'),
        ('work', 'work'),
        ('health', 'health')
    ))

    class Meta:
        model = Note
        fields = ['title', 'description', 'reminder', 'category']
