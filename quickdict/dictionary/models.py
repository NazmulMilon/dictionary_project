from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models


class Word(models.Model):
    word_name = models.CharField(max_length=100, help_text='word name')
    created_at = models.DateTimeField(auto_now_add=True, help_text='word created time added')
    updated_at = models.DateTimeField(auto_now=True, help_text='word name updated time')

    class Meta:
        db_table = 'words'


class Meaning(models.Model):
    word_name = models.ForeignKey(Word, on_delete=models.CASCADE, help_text='Word name for meaning')
    meanings = models.CharField(max_length=200, help_text='meanings of words')
    created_at = models.DateTimeField(auto_now_add=True, help_text='word meaning created time')
    updated_at = models.DateTimeField(auto_now=True, help_text='word meaning updated time')

    # class Meta:
    #     db_table = 'meanings'
    def __str__(self):
        return str(self.word_name)
