from django.test import TestCase
from django.contrib.auth.models import User

from notes.models import Note, Category

class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(
            title = 'work'
        )

        Category.objects.create(
            title = 'home'
        )
    
    def test_creation(self):
        work_category = Category.objects.get(title='work')
        home_category = Category.objects.get(title='home')

        self.assertEqual(work_category.title, 'work')
        self.assertEqual(home_category.title, 'home')

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username='manager', password='some_password_for_manager')
        User.objects.create(username='admin', password='some_password_for_admin')
    
    def test_creation(self):
        manager = User.objects.get(username='manager')
        admin = User.objects.get(username='admin')

        self.assertEqual(manager.username, 'manager')
        self.assertEqual(admin.username, 'admin')

        self.assertEqual(manager.password, 'some_password_for_manager')
        self.assertEqual(admin.password, 'some_password_for_admin')


class NoteTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username='test_user', password='some_password_12345')
        work_category = Category.objects.create(title='work')
        health_category = Category.objects.create(title='health')
        
        Note.objects.create(
            title = 'Do homework', 
            description='Some desc', 
            reminder = '2024-02-10', 
            category = work_category,
            author = user
        )

        Note.objects.create(
            title = 'Visit doctor', 
            description='Some desc 2', 
            reminder = '2024-02-15', 
            category = health_category,
            author = user
        )
    
    def test_creation(self):
        note1 = Note.objects.get(title='Do homework')
        note2 = Note.objects.get(title='Visit doctor')

        self.assertEqual(note1.description, 'Some desc')
        self.assertEqual(note2.description, 'Some desc 2')

        self.assertEqual(note1.category.title,'work')
        self.assertEqual(note2.category.title, 'health')