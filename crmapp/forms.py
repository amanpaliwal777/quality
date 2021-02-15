from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreate(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']