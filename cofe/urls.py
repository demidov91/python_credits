from cofe.views import *
from django.conf.urls import patterns, url



urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^$', add_credit_request, name='new_credit_request'),
    url(r'^$', select_credit_product, name='select_credit_product'),


    url('^requests/$', list_credit_requests, name='credit_requests'),
    url('^committee/requests/$', list_credit_requests_for_committee, name='credit_requests'),

)