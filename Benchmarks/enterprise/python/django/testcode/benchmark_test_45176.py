# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


def BenchmarkTest45176(request):
    secret_value = 'config_secret_test_abc123'
    data, _sep, _rest = str(secret_value).partition('\x00')
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
