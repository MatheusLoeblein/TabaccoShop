from rest_framework import serializers

from .models import Product, Variation


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description_short', 'description_long',
                  'image', 'slug', 'price_marketing',
                  'price_marketing_promotional', 'type']


class VariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variation
        fields = ['product', 'name',
                  'price', 'price_promotional', 'stock']
