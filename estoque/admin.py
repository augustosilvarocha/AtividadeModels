from django.contrib import admin
from estoque.models import Produto
# Register your models here.


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'description', 'price', 'amount', 'creation_date']
    search_fields = ['name', 'code']
    list_filter = ['creation_date']
    ordering = ['creation_date']
admin.site.register(Produto, ProdutoAdmin)
    




