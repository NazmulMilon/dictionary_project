from django.contrib import admin
from .models import Word, Meaning, UserProfile


# Register your models here.

class WordAdmin(admin.ModelAdmin):
    list_display = ['word_name', 'created_at', 'updated_at']


admin.site.register(Word, WordAdmin)


class MeaningAdmin(admin.ModelAdmin):

    list_display = ['meanings', 'created_at', 'updated_at']


admin.site.register(Meaning, MeaningAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'date_of_birth']


admin.site.register(UserProfile, UserProfileAdmin)