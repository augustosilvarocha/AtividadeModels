from django.contrib import admin
from estoque.models import Produto, Fornecedor, Categoria

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'description', 'price', 'amount', 'creation_date', 'supplier']
    search_fields = ['name', 'code']
    list_filter = ['creation_date']
    ordering = ['creation_date']

class FornecedorAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email']
    search_fields = ['name', 'phone']
    list_filter = ['name']
    ordering = ['name']

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Fornecedor, FornecedorAdmin)
admin.site.register(Categoria, CategoriaAdmin)
    




