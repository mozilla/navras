from django import forms

from navras.conversions.models import Point


class PointForm(forms.ModelForm):

    class Meta:
        model = Point