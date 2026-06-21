# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os
import base64


def BenchmarkTest53141(request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = base64.b64decode(file_value).decode('utf-8', 'ignore')
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return JsonResponse({"saved": True})
