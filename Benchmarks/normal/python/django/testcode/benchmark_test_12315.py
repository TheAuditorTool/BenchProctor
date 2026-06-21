# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


def BenchmarkTest12315(request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data, _sep, _rest = str(file_value).partition('\x00')
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
