from django.urls import path

from . import views

app_name = 'product'

urlpatterns = [
    path('', views.ProductListViewApi.as_view(
        {'get': 'list'}), name='list'),
    path('<int:id>/', views.ProductDetailViewApi.as_view(), name='detail'),
    path('variant/<int:product>/',
         views.ProductVariantListViewApi.as_view({'get': 'list'}), name='variant')
]
