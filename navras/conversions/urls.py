from django.conf.urls import patterns, url


urlpatterns = patterns(
    'navras.conversions.views',

    url(r'^edit/$', 'point_edit', name='point_edit'),
)
