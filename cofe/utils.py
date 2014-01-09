from cofe.models import CreditProduct, CreditRequestNotes


def user_in_group(user, group_name):
    """
    user: *User* instance.
    group_name: *str*, group name.
    """
    return user.groups.filter(name=group_name)



def is_bankworker(user):
    return user_in_group(user, 'bank worker')

def is_committee(user):
    return user_in_group(user, 'committee')

def is_external_user(user):
    """
    returns: True if *user* is not authenticated or authenticated as external user. False otherwise.
    """
    return not (is_bankworker(user) or is_committee(user))

def is_client(user):
    """
    returns: True if *user* is authenticated as external user.
    """
    return user.is_authenticated() and is_external_user(user)

def get_available_credit_products(credit_request):
    return tuple(filter(lambda x: credit_request.try_credit_product(x), CreditProduct.objects.filter(is_enabled=True)))




