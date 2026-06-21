# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import keyring


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest19589(request):
    secret_value = 'feature_flag_value'
    data = default_blank(secret_value)
    store_cred = keyring.get_password('app', 'service-account')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return JsonResponse({"saved": True})
