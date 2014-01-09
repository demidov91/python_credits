from django.conf import settings
from django import forms
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string

from cofe.models import CreditRequest, CreditRequestProcessing, CreditRequestNotes
from cofe.utils import get_available_credit_products

class UserForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput,
        }


class CreditRequestForm(ModelForm):
    class Meta:
        model = CreditRequest
        widgets = {
            'additional_text_info': forms.Textarea,
        }
        exclude = ('credit_product', )

    additional_text_info = forms.CharField(required=False)

    _required_for_data = ('passport_id', 'amount', 'month_income', 'duration')

    def __init__(self, data=None, *args, **kwargs):
        super(CreditRequestForm, self).__init__(data, *args, **kwargs)
        for _required in self._required_for_data:
            self.fields[_required].required = True
        instance = kwargs.get('instance')
        if instance:
            self.fields['additional_text_info'].initial = instance.get_user_message()

    def clean(self):
        cleaned_data = super(CreditRequestForm, self).clean()
        if cleaned_data.get('credit_product'):
            return cleaned_data
        model_data = cleaned_data.copy()
        del model_data['additional_text_info']
        if not(get_available_credit_products(CreditRequest(**model_data))):
            raise forms.ValidationError(render_to_string('includes/error_no_credit_products_to_satisfy.html'))
        return cleaned_data

    def save(self, author=None, *args, **kwargs):
        instance = super(CreditRequestForm, self).save(*args, **kwargs)
        if author and not author.is_authenticated():
            author = None
        if kwargs.get('commit', True) and self.cleaned_data['additional_text_info']:
            instance.set_user_message(self.cleaned_data['additional_text_info'])
        return instance


class SelectCreditProductForm(ModelForm):
    class Meta:
        model = CreditRequest
        fields = ('credit_product', )


class UpdateCreditRequest(ModelForm):
    class Meta:
        model = CreditRequest
        widgets = {
            'amount': forms.TextInput(attrs={'class': 'amount'}),
            'duration': forms.TextInput(attrs={'class': 'duration'}),
            'credit_product': forms.Select(attrs={'class': 'select-credit-product'}),
            'month_income': forms.TextInput(attrs={'class': 'salary'}),

        }
    additional_text_info = forms.CharField(required=False)

    def __init__(self, data, instance, *args, **kwargs):
        super(UpdateCreditRequest, self).__init__(data,  *args, instance=instance, **kwargs)
        self.fields['additional_text_info'].initial = instance.get_user_message()


