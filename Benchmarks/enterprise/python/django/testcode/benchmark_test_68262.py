# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import keyring


def BenchmarkTest68262(request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    parts = []
    for token in str(prop_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    store_cred = keyring.get_password('app', 'service-account')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return JsonResponse({"saved": True})
