# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import keyring


def BenchmarkTest31731(request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    parts = str(yaml_value).split(',')
    data = ','.join(parts)
    store_cred = keyring.get_password('app', 'service-account')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return JsonResponse({"saved": True})
