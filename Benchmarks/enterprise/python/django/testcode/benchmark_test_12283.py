# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest12283(request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = file_value.decode('utf-8', 'ignore') if isinstance(file_value, bytes) else file_value
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return JsonResponse({"saved": True})
