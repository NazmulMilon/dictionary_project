import kwargs as kwargs
from django.shortcuts import render
from .models import Word, Meaning
from .serializers import WordSerializer, MeaningSerializer, WordMeaningCreationSerializer
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
        serializer = WordSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class WordRetrieveAPIView(RetrieveAPIView):
    serializer_class = WordSerializer
    queryset = Word.objects.all()

    def get(self, request, *args, **kwargs):
        word_object = self.queryset.get(pk=kwargs['pk'])
        if word_object is None:
            return Response({'details': 'No word in the dictionary. '}, status=status.HTTP_404_NOT_FOUND)
        serializer = WordSerializer(word_object)
        return Response(serializer.data, status=status.HTTP_200_OK)


# class MeaningCreateAPIView(CreateAPIView):
#     queryset = Meaning.objects.all()
#     serializer_class = MeaningSerializer
#
#     def post(self, request, *args, **kwargs):
#         data = request.data
#         serializer = MeaningSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)


# class MeaningsOfWordRetrieveAPIView()
class MeaningListAPIView(ListAPIView):
    queryset = Meaning.objects.all()
    serializer_class = MeaningSerializer

    def get(self, request, *args, **kwargs):
        queryset = Meaning.objects.all()
        serializer = MeaningSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MeaningRetrieveAPIView(RetrieveAPIView):
    serializer_class = MeaningSerializer
    queryset = Meaning.objects.all()

    def get(self, request, *args, **kwargs):
        meaning_obj = self.queryset.get(pk=kwargs['pk'])
        serializer = MeaningSerializer(meaning_obj, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MeaningCreateAPIView(CreateAPIView):
    serializer_class = WordMeaningCreationSerializer
    queryset = Meaning.objects.all()

    def post(self, request, *args, **kwargs):
        data = request.data
        word_name = data.get('word_name', None)
        meanings = data.get('meanings', [])

        if word_name is None or word_name == '':
            return Response(data="Word name is required", status=status.HTTP_406_NOT_ACCEPTABLE)

        if len(meanings) < 1:
            return Response(data="meaning is required", status=status.HTTP_406_NOT_ACCEPTABLE)

        word_obj = Word(word_name=word_name)
        word_obj.save()

        for meaning in meanings:
            meaning_obj = Meaning(word_id=word_obj.id, meanings=meaning)
            meaning_obj.save()

        return Response(data="Accepted", status=status.HTTP_201_CREATED)



