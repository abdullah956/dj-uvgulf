from django import forms
from .models import OperatorCertification

class OperatorCertificationForm(forms.ModelForm):
    class Meta:
        model = OperatorCertification
        fields = '__all__'
        widgets = {
            'issued_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'  # Adding Bootstrap class to style the input
            }),
            'expiry_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'  # Adding Bootstrap class to style the input
            }),
            # You can add more fields with specific Bootstrap styling here
        }
  # Apply Bootstrap classes to all fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Iterate over all fields and add the 'form-control' class
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})