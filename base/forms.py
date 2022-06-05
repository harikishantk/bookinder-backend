from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *

class ReaderCreationForm(UserCreationForm):
    class Meta:
        model = Reader
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
