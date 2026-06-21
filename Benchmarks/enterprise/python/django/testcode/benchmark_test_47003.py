# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest47003(request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = (lambda v: v.strip())(file_value)
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return JsonResponse({"saved": True})
