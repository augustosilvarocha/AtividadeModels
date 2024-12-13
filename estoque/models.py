from django.db import models

class Categoria(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome')

    def __str__(self):
        return self.name
    
class Fornecedor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome')
    phone = models.CharField(max_length=16, verbose_name='Telefone')
    email = models.EmailField(verbose_name='Email')

    def __str__(self):
        return self.name

class Produto(models.Model):
    name = models.CharField(max_length=30, verbose_name='Nome')
    code = models.CharField(max_length=30, verbose_name='Código')
    description = models.CharField(max_length=100, blank=True, null= True, verbose_name='Descrição')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Preço')
    amount = models.IntegerField()
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Data Criação')
    category = models.ManyToManyField(Categoria, verbose_name='Categoria')
    supplier = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, blank=False, null= False, verbose_name='Fornecedor')

    def __str__(self):
        return self.name
