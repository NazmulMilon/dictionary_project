from .models import Word, Meaning
from rest_framework.serializers import ModelSerializer


class WordSerializer(ModelSerializer):
    class Meta:
        model = Word
        exclude = ['created_at', 'updated_at']


class MeaningSerializer(ModelSerializer):
    class Meta:
        model = Meaning
        exclude = ['created_at', 'updated_at']
