# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


def BenchmarkTest00924(request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = (lambda v: v.strip())(file_value)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
