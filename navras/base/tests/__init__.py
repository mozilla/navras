import factory

from factory import fuzzy

from navras.base.models import Source, Area, Product, Point


class SourceFactory(factory.django.DjangoModelFactory):
    title = fuzzy.FuzzyText()
    url = fuzzy.FuzzyText()

    class Meta:
        model = Source


class AreaFactory(factory.django.DjangoModelFactory):
    title = fuzzy.FuzzyText()
    url = fuzzy.FuzzyText()

    class Meta:
        model = Area


class ProductFactory(factory.django.DjangoModelFactory):
    title = fuzzy.FuzzyText()
    url = fuzzy.FuzzyText()

    class Meta:
        model = Product


class PointFactory(factory.django.DjangoModelFactory):
    title = fuzzy.FuzzyText()
    source = factory.SubFactory(SourceFactory)
    area = factory.SubFactory(AreaFactory)
    product = factory.SubFactory(ProductFactory)

    @factory.post_generation
    def parents(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for parent in extracted:
                self.parent.add(parent)

    class Meta:
        model = Point