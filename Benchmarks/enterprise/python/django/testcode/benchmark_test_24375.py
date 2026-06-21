# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet
import os


def BenchmarkTest24375(request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    parts = []
    for token in str(file_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return JsonResponse({"saved": True})
