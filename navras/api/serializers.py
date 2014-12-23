from rest_framework import serializers

from navras.conversions.models import Point, Area, Source, Product


class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = ('title', 'quantity', 'source', 'area', 'product', 'parent')


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ('title', 'url')


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ('title', 'url')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'url')