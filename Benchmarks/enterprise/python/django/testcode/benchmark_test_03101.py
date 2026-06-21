# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest03101(request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(yaml_value).encode())
    return JsonResponse({"saved": True})
