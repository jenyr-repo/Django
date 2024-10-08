from django import forms
from .models import Reserve


class LogForm(forms.ModelForm):
    class Meta:
        model=Reserve
        fields='__all__'