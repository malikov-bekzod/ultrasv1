from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "color",
            "size",
            "price",
            "category",
            "brand",
            "count",
            "types",
            "image",
            "gender",
        ]
