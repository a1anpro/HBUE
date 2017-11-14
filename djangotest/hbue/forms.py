from django.forms import forms
from django.forms.widgets import *

class FileUploadForm(forms.Form):
    icon = forms.FileField(
        widget=FileInput(attrs={
            'id': 'thumbnail'
        }),
        required=False,
    )

    # info = forms.CharField()