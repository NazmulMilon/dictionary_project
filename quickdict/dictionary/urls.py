from django.urls import path
from .views import *
# app_name = 'dictionary'
urlpatterns = [
    path('word/create/', WordCreateAPIView.as_view(), name='word_create'),
    # path('list/all/', WordCreateAPIView.as_view(), name='word_create'),
]
