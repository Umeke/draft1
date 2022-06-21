from rest_framework.generics import ListAPIView, RetrieveAPIView

from rest_framework import mixins

from rest_framework import generics

from shop.models import Shop, Category,Product

from shop.serializers import ShopSerializer, CategorySerializer, ProductSerializer


class ShopListView(ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class ShopDetailView(RetrieveAPIView):
    lookup_field = 'shop_id'
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(RetrieveAPIView):
    lookup_field = 'id'
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(RetrieveAPIView):
    lookup_field = 'id'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ShopList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


