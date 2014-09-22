from django.contrib.auth.decorators import user_passes_test

def venmo_authorized(function):
    dec = user_passes_test(lambda u: u.profile.is_venmo_authorized(), login_url='/profile')
    return dec(function)