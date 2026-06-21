# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


def BenchmarkTest20791(request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    def normalize(value):
        return value.strip()
    data = normalize(file_value)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
