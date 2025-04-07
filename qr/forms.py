from django import forms
from .models import OperatorCertification

class OperatorCertificationForm(forms.ModelForm):
    class Meta:
        model = OperatorCertification
        fields = '__all__'
        widgets = {
            'issued_date': forms.DateInput(attrs={'type': 'date'}),
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
        }
