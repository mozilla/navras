from django.conf.urls import patterns, url, include
from rest_framework import routers

from navras.api import views


router = routers.DefaultRouter()

router.register(r'points', views.PointView)
router.register(r'areas', views.AreaView)
router.register(r'sources', views.SourcelliteView)
router.register(r'products', views.ProductView)

urlpatterns = patterns(
    '',
    url(r'^', include(router.urls))
)
