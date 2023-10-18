from django import forms
from .models import file_column
class FileColumnForm(forms.ModelForm):
    class Meta:
        model=file_column
        fields='__all__'
