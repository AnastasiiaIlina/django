from django.test import TestCase
from notes.models import Note

class NoteTestCase(TestCase):
    def setUp(self):
        Note.objects.create(
            title = 'Do homework', 
            description='Some desc', 
            reminder = '2024-02-10', 
            category = 'work'
        )

        Note.objects.create(
            title = 'Visit doctor', 
            description='Some desc 2', 
            reminder = '2024-02-15', 
            category = 'health'
        )
    
    def test_creation(self):
        note1 = Note.objects.get(title='Do homework')
        note2 = Note.objects.get(title='Visit doctor')

        self.assertEqual(note1.description, 'Some desc 2')
        self.assertEqual(note2.description, 'Some desc 2')

        self.assertEqual(note1.category,'work')
        self.assertEqual(note2.category, 'health')



