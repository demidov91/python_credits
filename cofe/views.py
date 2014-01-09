from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout as django_logout
from django.db import transaction
from django.contrib.auth.decorators import login_required

from cofe.utils import is_external_user, is_bankworker, is_committee, is_client
from cofe.forms import UserForm, CreditRequestForm, SelectCreditProductForm, UpdateCreditRequest
from cofe.models import CreditProduct, CreditRequest

from cofe.utils import get_available_credit_products

def index(request):
    template_name = 'home.html'
    context = {}
    if request.user.is_authenticated():
        if is_bankworker(request.user) or is_committee(request.user):
            return redirect('credit_requests')
        if is_client(request.user):
            template_name = 'user_index.html'
            credit_request_id = request.session.get('last_created_request_id')
            if credit_request_id:
                try:
                    CreditRequest.objects.filter(id=credit_request_id).update(user=request.user)
                except CreditRequest.DoesNotExist:
                    pass
                finally:
                    del request.session['last_created_request_id']
            if CreditRequest.objects.filter(user=request.user).exists():
                context['has_loan_requests'] = True
    return render(request, template_name, context)


@login_required
def list_credit_requests(request):
    """
    *request* GET parameters can contains passport_id to filter results.
    """
    if is_client(request.user):
        credit_requests = CreditRequest.objects.filter(user=request.user)
    else:
        credit_requests = CreditRequest.objects.filter(**dict(request.GET.items()))
    return render(request, 'list_credit_requests.html', {
        'credit_requests': tuple((credit_request, UpdateCreditRequest(None, credit_request)) for credit_request in credit_requests),
        'filter': dict(request.GET.items()),
    })


def add_credit_request(request, credit_request_id=None):
    template_name = 'new_credit_request.html'
    instance=get_object_or_404(CreditRequest, id=credit_request_id) if credit_request_id else None
    if request.method == 'GET':
        form = CreditRequestForm(instance=instance) if credit_request_id else CreditRequestForm()
    elif request.method == 'POST':
        form = CreditRequestForm(request.POST, instance=instance)
        if form.is_valid():
            model = form.save(author=request.user)
            if not instance or not instance.credit_product:
                return redirect('select_credit_product', credit_request_id=model.id)
            else:
                return redirect('credit_request_was_created', credit_request_id=model.id)
    return render(request, template_name, {'form': form})

def update_credit_request(request, credit_request_id, form_class=UpdateCreditRequest):
    instance = get_object_or_404(CreditRequest, id=credit_request_id)
    form = form_class(request.POST, instance=instance)
    if form.is_valid():
        model = form.save()
        return render(request, 'includes/credit_request_row.html', {'credit_request': model, 'form': form})
    else:
        return render(request, 'includes/credit_request_row.html', {'credit_request': instance, 'form': form})



def select_credit_product(request, credit_request_id=None):
    if request.method == 'GET':
        if credit_request_id:
            credit_products = get_available_credit_products(CreditRequest.objects.get(id=credit_request_id))
        else:
            credit_products = CreditProduct.objects.filter(is_enabled=True)
        return render(request, 'list_credit_products.html', {
            'credit_products': credit_products,
            'credit_request_id': credit_request_id,
        })
    else:
        if credit_request_id:
            instance = get_object_or_404(CreditRequest, id=credit_request_id)
            SelectCreditProductForm(request.POST, instance=instance).save()
            return redirect('credit_request_was_created', credit_request_id=credit_request_id)
        model = SelectCreditProductForm(request.POST).save()
        return redirect('new_credit_request', credit_request_id=model.id)

def credit_request_was_created(request, credit_request_id):
    if not request.user.is_authenticated():
        request.session['last_created_request_id'] = credit_request_id
    return render(request, 'credit_request_was_created.html', {
        'credit_request': get_object_or_404(CreditRequest, id=credit_request_id),
    })

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