from django import forms
from estoque import models

class ProdutoForms(forms.Form):
    name = forms.CharField(label="Nome")
    code = forms.CharField(label="Código")
    description = forms.CharField(label="Descrição")
    price = forms.DecimalField(label="Preço")
    amount = forms.IntegerField(label="Quantidade")
    category = forms.ModelMultipleChoiceField(queryset=models.Categoria.objects.all())
    supplier = forms.ModelChoiceField(queryset=models.Fornecedor.objects.all())


class FornecedorForms(forms.Form):
    name = forms.CharField(label="Nome")
    phone = forms.CharField(label="Telefone")
    email = forms.EmailField(label="Email")


class CategoriaForms(forms.Form):
    name = forms.CharField(label="Categoria")


    