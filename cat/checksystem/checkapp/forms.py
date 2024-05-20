from django import forms
from .models import *

class writechecker(forms.ModelForm):
    class Meta:
        model = checker
        fields = ('__all__')


class checkin(forms.ModelForm):
    class Meta:
        model = checking
        fields = ('__all__')

        
class checkout(forms.ModelForm):
    class Meta:
        model = check_record
        fields = ('__all__')