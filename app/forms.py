from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
class RepasForm(forms.ModelForm):
    
    class Meta:
        model = Repas
        fields = ('__all__')

class RegistrationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('first_name','last_name',"username",'email',"password1",'password2',)

class MenuForm(forms.ModelForm):
    
    class Meta:
        model = Menu
        fields = ('__all__')
