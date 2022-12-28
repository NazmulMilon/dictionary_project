from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, help_text='user name')
    phone_number = models.IntegerField(default=False)
    date_of_birth = models.DateField(auto_now=False)

    class Meta:
        db_table = 'user_profiles'
