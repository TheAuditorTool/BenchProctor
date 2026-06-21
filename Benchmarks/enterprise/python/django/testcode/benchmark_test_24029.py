# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


def BenchmarkTest24029(request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    parts = str(secret_value).split(',')
    data = ','.join(parts)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
