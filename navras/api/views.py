from rest_framework import viewsets

from navras.api import serializers
from navras.conversions.models import Point, Area, Source, Product


class PointView(viewsets.ModelViewSet):
    queryset = Point.objects.all()
    serializer_class = serializers.PointSerializer


class AreaView(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = serializers.AreaSerializer


class SourcelliteView(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = serializers.SourceSerializer


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
