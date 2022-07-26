from cProfile import label
from django import forms
from .models import FileModel,AbstractUser

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = FileModel
        fields = ['name','fileurl']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'fileurl': forms.FileInput(attrs={'class':'form-control'}),
        }

