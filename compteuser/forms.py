from django.contrib.auth import UserCreationForm
from django.contrib.auth import User
from django import forms


class UserForm(UserCreationForm):
    class meta:
        model = User
        fields = ["username","password"]