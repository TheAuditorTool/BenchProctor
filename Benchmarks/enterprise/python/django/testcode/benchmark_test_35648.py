# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


def BenchmarkTest35648(request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    prefix = ''
    data = prefix + str(file_value)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
