from django import forms
from  .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
           "title",
           "description",
           "price"
        ]


class django_standard_form(forms.Form):
    title = forms.CharField(max_length=120)
    description = forms.CharField(max_length=400)
    price = forms.DecimalField(max_digits=10000, decimal_places=2)