from cofe.views import *
from django.conf.urls import patterns, url



urlpatterns = patterns('',
    url(r'login/$', 'django.contrib.auth.views.login', {
        'template_name': 'login.html',
        }, name='custom_logon'),
    url(r'^logout/$', logout, name='logout'),

    url(r'^register/$', register, name='register'),

    url(r'^$', index, name='index'),
    url(r'^$', add_credit_request, name='new_credit_request'),
    url(r'^$', select_credit_product, name='select_credit_product'),


    url('^requests/$', list_credit_requests, name='credit_requests'),

)