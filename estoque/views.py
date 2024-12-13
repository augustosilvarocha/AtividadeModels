from django.shortcuts import render
from estoque import models

# Create your views here.

def Index(request):
    return render(request, 'index.html')

def List(request, choice):
    if choice == 'produtos':
        produtos = models.Produto.objects.all()
        context = {'produtos':produtos}

    elif choice == 'fornecedores':
        fornecedores = models.Fornecedor.objects.all()
        context = {'fornecedores':fornecedores}

    elif choice == 'categorias':
        categorias = models.Categoria.objects.all()
        context = {'categorias':categorias}

    return render(request, 'table.html', context)

def DetailProduct(request, pk):
    produto = models.Produto.objects.get(id=pk)
    context = {'produto': produto}
    return render(request, 'detail.html', context)
