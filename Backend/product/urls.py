from django.urls import path

from . import views

app_name = 'product'

urlpatterns = [
    path('', views.ProductListViewApi.as_view(
        {'get': 'list', 'post': 'create'}), name='list'),
    path('<str:id>/', views.ProductDetailViewApi.as_view(), name='detail'),
    path('variant/<str:id>/',
         views.ProductVariantListViewApi.as_view({'get': 'list'}), name='variant')
]
