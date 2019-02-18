from django import forms
from blog.models import UserProfileInfo
from django.contrib.auth.models import User
import re


def check_for_bitmail(value):
   if not re.match('f201[0-9][0-9]*4@pilani.bits-pilani.ac.in', value):
        raise forms.ValidationError("Not a bitsian!")


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField(validators=[check_for_bitmail])
    class Meta():
        model = User
        fields = ('username','email','password',)

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('picture',)










