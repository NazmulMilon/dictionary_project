from django.urls import path
from .views import *
# app_name = 'dictionary'
urlpatterns = [
    path('word/create/', WordCreateAPIView.as_view(), name='word_create'),
    path('word/list/', WordListAPIView.as_view(), name='all_word_list'),
    path('word/details/<int:pk>/', WordRetrieveAPIView.as_view(), name='word_details'),


    path('word/meaning/create/', MeaningCreateAPIView.as_view(), name='word_create'),
    path('meaning/list/', MeaningListAPIView.as_view(), name='all_meaning_list'),
    path('meaning/details/<int:pk>/', MeaningRetrieveAPIView.as_view(), name='all_meaning_list'),
    path("search/word/<str:word_name>/", WordMeaningSearch.as_view(), name='search_meaning_for_word'),
    # path('word/<str:word_name>/meaning/create/', MeaningCreateAPIView.as_view(), name='word_create'),
]
