from django.conf.urls import patterns, include, url
from CMF.views import MoneyDetail

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LMT.views.home', name='home'),
    # url(r'^LMT/', include('LMT.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^money_detail/(?P<pk>[\d-]+)/$', MoneyDetail.as_view()),
)
