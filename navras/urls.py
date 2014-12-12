from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Admin
    url(r'^admin/', include(admin.site.urls)),
)
