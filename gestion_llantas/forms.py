from django import forms
from .models import llanta

class LlantaForm(forms.ModelForm):
    class Meta:
        model = llanta
        fields = '__all__'