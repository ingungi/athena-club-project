from django.shortcuts import render

from rest_framework.views import APIView, status
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer

class CarouselProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class getProduct(APIView):
    def get(self, request, format=None):
        item_id = request.GET.get('id')
        try:
            product = Product.objects.get(id=item_id)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data)