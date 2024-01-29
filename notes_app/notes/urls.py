from django.http import HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    path('favicon.ico', lambda request: HttpResponse(status=204)),

    path("", views.return_home_page, name="home_page"),
    path("add/", views.return_add_note_page, name="add_note_page"),
    path("<str:id>/", views.return_one_note_page, name="one_note_page"),
    path("<str:id>/edit/", views.return_edit_note_page, name="edit_note_page"),
    path("<str:id>/delete/", views.return_delete_note_page, name="delete_note_page"),
]
