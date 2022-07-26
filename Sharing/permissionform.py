from django import forms
from .models import PermissionModel

class PermissionForm(forms.ModelForm):
    class Meta:
        model = PermissionModel
        fields = ['ruser']
        # widgets = {
        #     'ruser': forms.ModelChoiceField(attrs={'class':'form-control'})
        # }

