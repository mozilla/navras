from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Base
    url(r'^', include('navras.base.urls')),

    # Conversion
    url(r'^c/', include('navras.conversions.urls')),

    # Admin
    url(r'^admin/', include(admin.site.urls)),

    # Auth
    url(r'', include('django_browserid.urls')),

    # API
    url(r'^api/', include('navras.api.urls'))
)
