import kwargs as kwargs
from django.shortcuts import render
from .models import Word, Meaning
from .serializers import WordSerializer, MeaningSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.validators import ValidationError

class WordCreateAPIView(CreateAPIView):
    serializer_class = WordSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        word_name = data.get('word_name', None)
        if Word.objects.filter(word_name=word_name).exists():
            return Response(data={'details': 'Word Already Exists. '}, status=status.HTTP_406_NOT_ACCEPTABLE)

        word_name = Word(word_name=word_name)
        word_name.save()
        return Response(data={'details': 'New Word Added to the Dictionary'}, status=status.HTTP_201_CREATED)


class WordListAPIView(ListAPIView):
    serializer_class = WordSerializer
    queryset = Word.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = Word.objects.all()
        serialize = WordSerializer(queryset, many=True)
        return Response(serialize.data, status=status.HTTP_200_OK)


class WordRetrieveAPIView(RetrieveAPIView):
    serializer_class = WordSerializer
    queryset = Word.objects.all()

    def get(self, request, *args, **kwargs):
        word_name = self.queryset.filter(pk=kwargs['pk']).first()
        if word_name is None:
            return Response({'details': 'No word in the dictionary. '}, status=status.HTTP_404_NOT_FOUND)
        serialize = WordSerializer(word_name)
        return Response(serialize.data, status=status.HTTP_200_OK)
