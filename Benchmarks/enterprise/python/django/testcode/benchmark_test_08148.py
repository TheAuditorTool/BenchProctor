# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import keyring


def BenchmarkTest08148(request):
    secret_value = 'default_setting_value'
    data = '%s' % str(secret_value)
    store_cred = keyring.get_password('app', 'service-account')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return JsonResponse({"saved": True})
