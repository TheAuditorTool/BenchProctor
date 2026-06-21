# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


def BenchmarkTest29550(request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = ' '.join(str(file_value).split())
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
