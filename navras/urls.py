from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Base urls
    url(r'^', include('navras.base.urls')),

    # Admin
    url(r'^admin/', include(admin.site.urls)),
)
