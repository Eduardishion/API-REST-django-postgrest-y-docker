from rest_framework import serializers

from .models import product

class productsSerializer(serializers.ModelSerializer):
    class Meta:
        model  = product
        fields = ('name','brand', 'created_at', 'updated_at')
