from django.shortcuts import render

from navras.conversions.forms import PointForm
from navras.conversions.models import Source, Area, Product


def point_edit(request):
    form = PointForm()
    areas = Area.objects.all()
    products = Product.objects.all()
    sources = Source.objects.all()
    return render(request, 'point_edit.html', {'form': form, 'products': products,
                                               'sources': sources, 'areas': areas})
