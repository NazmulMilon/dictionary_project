from django.contrib import admin
from .models import Word, Meaning


# Register your models here.

class WordAdmin(admin.ModelAdmin):
    list_display = ('word_name', 'created_at', 'updated_at')


admin.site.register(Word, WordAdmin)


class MeaningAdmin(admin.ModelAdmin):

    list_display = ('meanings', 'created_at', 'updated_at')


admin.site.register(Meaning, MeaningAdmin)

