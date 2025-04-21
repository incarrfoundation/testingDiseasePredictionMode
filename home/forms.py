from django import forms
from .models import UploadedImage

class UploadForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = ['image']
