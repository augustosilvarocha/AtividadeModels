from django.shortcuts import render
from estoque import models
from .forms import ProdutoForms, FornecedorForms, CategoriaForms
from django.urls import reverse
from django.shortcuts import redirect


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

def create_product(request):
    if request.method =="POST":
        form = ProdutoForms(request.POST)
        if form.is_valid():
            produto = models.Produto(
                name=form.cleaned_data['name'],
                code=form.cleaned_data['code'],
                description=form.cleaned_data.get('description'),  
                price=form.cleaned_data['price'],
                amount=form.cleaned_data['amount'],
                supplier=form.cleaned_data['supplier']
            )
            produto.save()
            produto.category.set(form.cleaned_data['category'])
            return redirect('listing', 'categorias')
    else:
        form = ProdutoForms()
        return render(request, "forms/formulario_produto.html", {'form':form})
    
def create_supplier(request):
    if request.method =="POST":
        form = FornecedorForms(request.POST)
        if form.is_valid():
            supplier = models.Fornecedor(
                name = form.cleaned_data['name'],
                phone = form.cleaned_data['phone'],
                email = form.cleaned_data['email'],
            )
            supplier.save()
            return redirect('listing', 'fornecedores')
    else:
        form = FornecedorForms()
        return render(request, "forms/formulario_fornecedor.html", {'form':form})
    

def create_category(request):
    if request.method == "POST":
        form = CategoriaForms(request.POST)
        if form.is_valid():
            category = models.Categoria(
                name = form.cleaned_data['name'],
            )
            category.save()
            return redirect('listing', 'categorias')
    else:
        form = CategoriaForms()
        return render(request, "forms/formulario_categoria.html", {'form':form})

