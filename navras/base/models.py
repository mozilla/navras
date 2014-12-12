from django.db import models


class Source(models.Model):
    """Model for Data Sources"""
    title = models.CharField(max_length=100)
    url = models.URLField(max_length=255, blank=True, null=True)


class Area(models.Model):
    """Model for Functional Areas"""
    title = models.CharField(max_length=100)
    url = models.URLField(max_length=255, blank=True, null=True)


class Product(models.Model):
    """Model for Products"""
    title = models.CharField(max_length=100)
    url = models.URLField(max_length=255, blank=True, null=True)


class Point(models.Model):
    """Model for Conversion Points"""
    title = models.CharField(max_length=100)
    source = models.ForeignKey(Source)
    area = models.ForeignKey(Area, blank=True, null=True,
                               on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, blank=True, null=True,
                               on_delete=models.SET_NULL)
    parent = models.ManyToManyField('self', blank=True, null=True,
                                    related_name='points_children_set')
