from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import product
from .serializers import productsSerializer


#listar todos los productos
class listProducts(generics.ListCreateAPIView):

    queryset = product.objects.all()
    serializer_class = productsSerializer

#listar un producto
class detailProduct(generics.RetrieveAPIView):
    queryset = product.objects.all()
    serializer_class = productsSerializer

#crear producto
class createProduct(generics.CreateAPIView):
    queryset = product.objects.all()
    serializer_class = productsSerializer


class updateProduct(generics.RetrieveUpdateAPIView):
    queryset = product.objects.all()
    serializer_class = productsSerializer


class deleteProduct(generics.DestroyAPIView):
    queryset = product.objects.all()
    serializer_class = productsSerializer

