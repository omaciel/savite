from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = "username",


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = "username",

