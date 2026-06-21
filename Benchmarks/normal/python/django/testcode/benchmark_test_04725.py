# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


def ensure_str(value):
    return str(value)

def BenchmarkTest04725(request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = ensure_str(file_value)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
