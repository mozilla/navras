from django.conf.urls import patterns, url
from django.views.generic import TemplateView


urlpatterns = patterns(
    'navras.base.views',
    url(r'^$', 'home', name='home'),
)
