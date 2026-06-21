# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


def BenchmarkTest61357(request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    def normalize(value):
        return value.strip()
    data = normalize(secret_value)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
