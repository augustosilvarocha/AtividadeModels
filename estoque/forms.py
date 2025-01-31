from django import forms
from estoque import models
from django.core.exceptions import ValidationError
import re

class ProdutoForms(forms.Form):
    name = forms.CharField(label="Nome")
    code = forms.CharField(label="Código")
    description = forms.CharField(label="Descrição")
    price = forms.DecimalField(label="Preço")
    amount = forms.IntegerField(label="Quantidade", min_value=0)
    category = forms.ModelMultipleChoiceField(queryset=models.Categoria.objects.all())
    supplier = forms.ModelChoiceField(queryset=models.Fornecedor.objects.all())

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise ValidationError("O nome deve conter pelo menos 3 caracteres.")
        return name

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise ValidationError("O preço do produto deve ser maior que zero.")
        return price

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount < 0:
            raise ValidationError("A quantidade não pode ser negativa.")
        return amount

    def clean_code(self):
        code = self.cleaned_data.get('code')
        if not re.match(r'^[a-zA-Z\d]+$', code):
            raise ValidationError("O código do produto deve conter apenas letras e números.")
        return code

class FornecedorForms(forms.Form):
    name = forms.CharField(label="Nome")
    phone = forms.CharField(label="Telefone")
    email = forms.EmailField(label="Email")

class CategoriaForms(forms.Form):
    name = forms.CharField(label="Categoria")


    