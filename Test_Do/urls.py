from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about),
    path('api/v1/notes/', views.NoteGetView.as_view()),
    path('api/v1/notes/<int:note_id>', views.NoteDetailedGetView.as_view()),
    path('api/v1/add/', views.NotePostView.as_view()),
    path('api/v1/edit/<int:note_id>',views.NotePatchView.as_view()),
    path('api/v1/delete/<int:note_id>',views.NoteDeleteView.as_view()),
]