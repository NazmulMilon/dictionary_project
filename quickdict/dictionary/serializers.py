from .models import Word, Meaning
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class MeaningSerializer(ModelSerializer):
    class Meta:
        model = Meaning
        exclude = ['created_at', 'updated_at', 'word']


class WordSerializer(ModelSerializer):
    meanings = serializers.SerializerMethodField()

    def get_meanings(self, instance):
        meaning_queryset = Meaning.objects.filter(word_id=instance.id)
        return MeaningSerializer(meaning_queryset, many=True).data

    class Meta:
        model = Word
        # fields = ('id', 'word_name', 'meanings')
        exclude = ['created_at', 'updated_at']


class WordMeaningCreationSerializer(ModelSerializer):
    meanings = WordSerializer(many=True)

    class Meta:
        model = Word
        exclude = ['created_at', 'updated_at']
























#
# meanings = serializers.SerializerMethodField()
#
#    def get_meanings(self, instance):
#        meaning_queryset = Meaning.objects.filter(word_id=instance.id)
#        return MeaningSerializer(meaning_queryset, many=True).data
