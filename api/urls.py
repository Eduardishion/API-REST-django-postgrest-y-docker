from django.urls import path

from .views import listProducts, detailProduct,createProduct, updateProduct, deleteProduct

urlpatterns = [
    path('',listProducts.as_view()),#lista de productos
    path('<int:pk>', detailProduct.as_view()),#detalle por porducto
    path('create',createProduct.as_view()),#crear producto
    path('<int:pk>/update',updateProduct.as_view()),#actualisar producto
    path('<int:pk>/delete',deleteProduct.as_view()),#eliminar producto
]

