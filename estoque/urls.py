from django.urls import path
from estoque import views

urlpatterns = [
    path("", views.Index, name='index'),
    path("list/<str:choice>", views.List, name='listing'),
    path("detail/product/<int:pk>/", views.DetailProduct, name='detail-product'),
    path("create/product", views.create_product, name="create-product"),
    path("create/category", views.create_category, name="create-category"),
    path("create/supplier", views.create_supplier, name="create-supplier"),
]
