from django import forms

from .models import Work


class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ['name', 'description']
        help_text = {
            'name': '',
            'description': '',
        }
