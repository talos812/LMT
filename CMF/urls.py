from django.conf.urls import patterns, include, url
from CMF.views import MoneyDetail,Home,RequestDetail,History,MakeRequest,BeAcceptList,MoneyList
from django.contrib.auth.decorators import login_required
from django.views.generic.simple import direct_to_template
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LMT.views.home', name='home'),
    # url(r'^LMT/', include('LMT.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^home/$',login_required(Home.as_view(), redirect_field_name="next", login_url='/login/'),name="home"),
    url(r'^money_detail/(?P<pk>[\d-]+)/$', login_required(MoneyDetail.as_view(), redirect_field_name="next", login_url='/login/'), name="money_detail"),
    url(r'^request_detail/(?P<pk>[\d-]+)/$',login_required(RequestDetail.as_view(), redirect_field_name="next", login_url='/login/'),name="request_detail"),
    url(r'^request_history/$',login_required(History.as_view(), redirect_field_name="next", login_url='/login/'),name="request_detail"),
    url(r'^request_create/$',login_required(MakeRequest.as_view(), redirect_field_name="next", login_url='/login/'),name="request_create"),
    url(r'^be_accept_list/$',login_required(BeAcceptList.as_view(), redirect_field_name="next", login_url='/login/'), name="be_request_list"),
    url(r'^money_list/$',login_required(MoneyList.as_view(), redirect_field_name="next", login_url='/login/'), name="money_list"),
    url(r'^accept_suc/$',direct_to_template,{'template':'CMF/accept_suc.html'}),
    url(r'^accept_fail/$',direct_to_template,{'template':'CMF/accept_fail.html'}),
    url(r'^help/$',direct_to_template,{'template':'CMF/help.html'},name="help"),
)
