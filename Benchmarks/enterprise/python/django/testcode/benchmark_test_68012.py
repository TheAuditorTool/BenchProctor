# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


def to_text(value):
    return str(value).strip()

def BenchmarkTest68012(request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    data = to_text(secret_value)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
