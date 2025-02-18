# uploadphoto/forms.py
from django import forms
from .models import UserPhoto

class UserPhotoForm(forms.ModelForm):
    class Meta:
        model = UserPhoto
        fields = ['image', 'place_name', 'address']
