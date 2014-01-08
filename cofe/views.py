from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout as django_logout
from django.db import transaction

from cofe.utils import is_external_user, is_bankworker, is_committee, is_client
from cofe.forms import UserForm

def index(request):
    template_name = 'home.html'
    if request.user.is_authenticated():
        if is_bankworker(request.user) or is_committee(request.user):
            return redirect('credit_requests')
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

@transaction.atomic
def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request=request, user=new_user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})

def logout(request):
    if request.method == 'POST':
        django_logout(request)
    return redirect('index')