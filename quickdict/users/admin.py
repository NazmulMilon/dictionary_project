from django.contrib import admin
from .models import UserProfile
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    fields = ['user', 'phone_number', 'date_of_birth']


admin.site.register(UserProfile, UserProfileAdmin)
