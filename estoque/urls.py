from django.urls import path
from estoque import views

urlpatterns = [
    path("", views.Index, name='index'),
    path("create/product", views.create_product, name="create-product"),
    path("create/category", views.create_category, name="create-category"),
    path("create/supplier", views.create_supplier, name="create-supplier"),
    path("detail/product/<int:pk>/", views.DetailProduct, name='detail-product'),
    path("product/list", views.ProdutoListView.as_view(), name="list-product"),
    path("category/list", views.CategoriaListView.as_view(), name="list-category"),
    path("supplier/list", views.FornecedorListView.as_view(), name="list-supplier"),
]
