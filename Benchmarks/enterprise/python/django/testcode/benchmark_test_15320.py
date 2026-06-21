# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


def BenchmarkTest15320(request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    data = f'{secret_value}'
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
