from .views import NoteDetail, NoteList
from django.urls import path


urlpatterns = [
    path('notes/', NoteList.as_view(), name='Notes'),
    path('notes/<int:pk>', NoteDetail.as_view(), name='Note Detail')
]
