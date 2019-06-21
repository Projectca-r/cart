from django import forms
from .models import *

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['cartitem', 'decimal']
    
    def save(self):
        new_cart = Cart.objects.create(
            cartitem=self.cleaned_data['cartitem'],
            decimal=self.cleaned_data['decimal'],
        )
        return new_cart