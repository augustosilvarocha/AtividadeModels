from django.urls import path
from estoque import views

urlpatterns = [
    path("", views.Index, name='index'),
    path("list/<str:choice>", views.List, name='listing'),
    path("detail/product/<int:pk>/", views.DetailProduct, name='detail-product'),
]
