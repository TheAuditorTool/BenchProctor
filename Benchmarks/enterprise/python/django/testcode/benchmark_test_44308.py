# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


def BenchmarkTest44308(request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    Fernet(file_value.encode() if isinstance(file_value, str) else file_value).encrypt(b'data')
    return JsonResponse({"saved": True})
