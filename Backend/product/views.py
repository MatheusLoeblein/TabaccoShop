from django.http import Http404
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Product, Variation
from .serializers import ProductSerializer, VariationSerializer

# Create your views here.


class ProductListViewApi(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    http_method_names = ['get', 'post', 'options', 'head']

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class ProductDetailViewApi(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'


class ProductVariantListViewApi(ModelViewSet):
    queryset = Variation.objects.all()
    serializer_class = VariationSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(product__id=self.kwargs.get('product'))

        if not qs.exists():
            raise Http404("Not found.")
        return qs
