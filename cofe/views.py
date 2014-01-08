from django.shortcuts import render, redirect
from cofe.utils import is_external_user, is_bankworker, is_committee, is_client

def index(request):
    template_name = 'home.html'
    if request.user.is_authenticated():
        if is_bankworker(request.user):
            return redirect('credit_requests')
        if is_committee(request.user):
            return redirect('credit_requests_for_committee')
        if is_client(request.user):
            template_name = 'user_index.html'
    return render(request, template_name)


def list_credit_requests(request):
    """
    *request* GET parameters can contains passport_id to filter results.
    """
    pass

def list_credit_requests_for_committee(request):
    """
    *request* GET parameters can contains passport_id to filter results.
    """
    pass



def add_credit_request(request):
    pass

def select_credit_product(request):
    pass