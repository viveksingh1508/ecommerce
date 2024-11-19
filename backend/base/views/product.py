from rest_framework.decorators import api_view
from base.models import Product
from base.serializers import ProductSerializer
from rest_framework.response import Response


@api_view(["GET"])
def getProducts(request):
    products = Product.objects.all()
    serailizer = ProductSerializer(products, many=True)
    return Response(serailizer.data)


@api_view(["GET"])
def getProduct(request, pk):
    product = Product.objects.get(_id=pk)
    serailizer = ProductSerializer(product, many=False)
    return Response(serailizer.data)
