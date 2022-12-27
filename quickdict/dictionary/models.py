from django.db import models


# Create your models here.

class Word(models.Model):
    word_name = models.CharField(max_length=100, help_text='word name')
    created_at = models.DateTimeField(auto_now_add=True, help_text='word created time added')
    updated_at = models.DateTimeField(auto_now=True, help_text='word name updated time')

    def __str__(self):
        return self.word_name


class Meaning(models.Model):
    word_name = models.ForeignKey(Word, on_delete=models.CASCADE, help_text='Word name for meaning')
    meanings = models.CharField(max_length=200, help_text='meanings of words')
    created_at = models.DateTimeField(auto_now_add=True, help_text='word meaning created time')
    updated_at = models.DateTimeField(auto_now=True, help_text='word meaning updated time')

    # def __str__(self):
    #     return self.word_name
