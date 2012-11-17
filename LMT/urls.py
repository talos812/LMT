from django.conf.urls import patterns, include, url
from CMF import urls as cmf_urls
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.auth.views import login
from CMF.views import logout_view
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LMT.views.home', name='home'),
    # url(r'^LMT/', include('LMT.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cmf/',include(cmf_urls)),
    url(r'^login/$',login),
    url(r'^logout/$',logout_view),
)
