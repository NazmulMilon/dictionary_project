from django.urls import path
from .views import *
# app_name = 'dictionary'
urlpatterns = [
    path('word/create/', WordCreateAPIView.as_view(), name='word_create'),
    path('word/list/', WordListAPIView.as_view(), name='word_list_all'),
    path('word/<int:pk>/', WordRetrieveAPIView.as_view(), name='word_details'),


    # path('word/meaning/created/', MeaningCreateAPIView.as_view(), name='word_create'),
]
