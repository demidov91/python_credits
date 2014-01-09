from cofe.utils import is_client, is_bankworker, is_committee, is_external_user

def context_processor(request):
    return {
        'is_client': is_client(request.user),
        'is_bankworker': is_bankworker(request.user),
        'is_committee': is_committee(request.user),
        'is_external': is_external_user(request.user),
    }