# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import keyring


def BenchmarkTest05299(request):
    secret_value = 'app_display_name'
    data = secret_value if secret_value else 'default'
    store_cred = keyring.get_password('app', 'service-account')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return JsonResponse({"saved": True})
