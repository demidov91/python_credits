from django.conf import settings
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext as _
from django.template.loader import render_to_string


class CreditProduct(models.Model):
    ACCEPT_RULE_NO_COMMITTEE = 0
    ACCEPT_RULE_ONE_COMMITTEE_MEMBER = 1
    ACCEPT_RULE_TWO_COMMITTEE_MEMBERS = 2
    ACCEPT_RULE_HALF_COMMITTEE_MEMBERS = 3
    ACCEPT_RULE_MORE_THEN_HALF_COMMITTEE_MEMBERS = 4
    ACCEPT_RULE_OTHER = 5

    ACCEPT_RULE_CHOICES = (
        (ACCEPT_RULE_NO_COMMITTEE, _('by bank worker')),
        (ACCEPT_RULE_ONE_COMMITTEE_MEMBER, _('one_check')),
        (ACCEPT_RULE_TWO_COMMITTEE_MEMBERS, _('committee_double_check')),
        (ACCEPT_RULE_HALF_COMMITTEE_MEMBERS, _('half_of_active_committee_members')),
        (ACCEPT_RULE_MORE_THEN_HALF_COMMITTEE_MEMBERS, _('half_of_active_committee_members_plus_one')),
        (ACCEPT_RULE_OTHER, _('other')),
    )

    KIND_ANNUITY = 0
    KIND_FACTICAL = 1
    KIND_PERCENTS = 2

    KIND_CHOICES = (
        (KIND_ANNUITY, _('ANNUITY')),
        (KIND_FACTICAL, _('FACTICAL')),
        (KIND_PERCENTS, _('PERCENTS')),
    )

    name = models.CharField(max_length=120, null=False)
    is_enabled = models.BooleanField(default=False)

    require_no_military_duty = models.BooleanField(blank=True, default=False)
    max_age = models.PositiveSmallIntegerField(null=True, blank=True)
    min_age = models.PositiveSmallIntegerField(null=True, blank=True)
    #*min_pure_month_income* <= 2147483647 !
    min_pure_month_income = models.IntegerField(null=True, blank=True)
    #*max_amount* <= 2147483647 !
    max_amount = models.IntegerField()
    accept_rule = models.PositiveSmallIntegerField(choices=ACCEPT_RULE_CHOICES)
    #kind of payments
    kind = models.PositiveSmallIntegerField(choices=KIND_CHOICES, null=False, default=KIND_FACTICAL)

    #%. usually, between 0 and 100, but can be higher.
    rate = models.DecimalField(null=False, decimal_places=6, max_digits=11, default=20)
    min_month_duration = models.PositiveSmallIntegerField(null=True, blank=True)
    max_month_duration = models.PositiveSmallIntegerField(null=True, blank=True)

    other_requirements = models.TextField(null=True, blank=True)

    def get_verbose_kind(self):
        return render_to_string('includes/get_credit_verbose_name.html', {'credit': self})





class CreditRequest(models.Model):
    passport_id = models.CharField(validators=[RegexValidator(regex='[A-Z]{2}\d{7}'), ], max_length=9, null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    credit_product = models.ForeignKey(CreditProduct)
    amount = models.IntegerField(null=False)


class Credit(models.Model):
    STATE_DRAFT = 0
    STATE_ACTIVE = 1
    STATE_PAYED_IN_TIME = 2
    STATE_PAYED_BEFORE_TIME = 3
    STATE_CLOSED_AS_PROBLEM = 4

    STATE_CHOICES = (
        (STATE_DRAFT, _('draft')),
        (STATE_ACTIVE, _('active')),
        (STATE_PAYED_IN_TIME, _('payed_in_time')),
        (STATE_PAYED_BEFORE_TIME, _('payed_before_time')),
        (STATE_CLOSED_AS_PROBLEM, _('closed_as_problem')),
    )
    state = models.PositiveSmallIntegerField(choices=STATE_CHOICES, null=False)


class CreditRequestProcessing(models.Model):
    ACCEPT_YES = 0
    ACCEPT_NO = 1
    ACCEPT_CANT_ANSWER = 2

    BANK_WORKER_CHOICES = (
        (ACCEPT_YES, _('yes')),
        (ACCEPT_NO, _('no')),
        (ACCEPT_CANT_ANSWER, _('reassign_to_committee')),
    )

    BANK_WORKER_CHOICES = (
        (ACCEPT_YES, _('yes')),
        (ACCEPT_NO, _('no')),
    )

    credit_request = models.OneToOneField(CreditRequest, null=False)
    credit = models.OneToOneField(Credit, null=True, blank=True)
    bank_worker_acceptance = models.PositiveSmallIntegerField(choices=BANK_WORKER_CHOICES, null=True, blank=True)
    committee_acceptance = models.PositiveSmallIntegerField(choices=BANK_WORKER_CHOICES, null=True, blank=True)


class CreditRequestNotes(models.Model):
    processing = models.ForeignKey(CreditRequestProcessing, null=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=False)
    message = models.TextField(null=False)



