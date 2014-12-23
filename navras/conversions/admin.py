from django.contrib import admin

from navras.conversions.models import Area, Product, Source, Point


class AreaAdmin(admin.ModelAdmin):
    list_display = ('title', )


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', )


class SourceAdmin(admin.ModelAdmin):
    list_display = ('title', )


class PointAdmin(admin.ModelAdmin):
    list_display = ('title', )

admin.site.register(Area, AreaAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(Point, PointAdmin)
