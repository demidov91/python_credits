from cofe.views import *
from django.conf.urls import patterns, url



urlpatterns = patterns('',
    url(r'login/$', 'django.contrib.auth.views.login', {
        'template_name': 'login.html',
        }, name='custom_logon'),
    url(r'^logout/$', logout, name='logout'),

    url(r'^register/$', register, name='register'),

    url(r'^$', index, name='index'),
    url(r'^request/add/$', add_credit_request, name='new_credit_request'),
    url(r'^request/add/(?P<credit_request_id>\d+)/$', add_credit_request, name='new_credit_request'),
    url(r'^credit-products$', select_credit_product, name='select_credit_product'),
    url(r'^credit-products/(?P<credit_request_id>\d+)/$', select_credit_product, name='select_credit_product'),
    url(r'^ajax/credit-request/(?P<credit_request_id>\d+)/update/$', update_credit_request, name='update_credit_request-ajax'),

    url(r'^credit-request/(?P<credit_request_id>\d+)/success/$', credit_request_was_created, name='credit_request_was_created'),

    url('^requests/$', list_credit_requests, name='credit_requests'),

)