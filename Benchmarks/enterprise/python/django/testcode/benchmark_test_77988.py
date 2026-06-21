# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import yaml


def BenchmarkTest77988(request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    data = f'{prop_value:.200s}'
    with open('/etc/app/secrets.yaml') as f:
        store_cred = yaml.safe_load(f)['secret']
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return JsonResponse({"saved": True})
