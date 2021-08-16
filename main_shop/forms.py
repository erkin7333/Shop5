from django import forms
from .models import Adress



class AdressForm(forms.ModelForm):
    class Meta:
        model = Adress
        fields = ('full_name', 'viloyat', 'tuman', 'mahalla', 'uy_raqami', 'phone')



