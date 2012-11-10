from django import forms
from CMF.models import Request

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['from_user', 'to_user', 'money', 'is_fill']