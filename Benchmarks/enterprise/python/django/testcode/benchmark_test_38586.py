# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


def normalise_input(value):
    return value.strip()

def BenchmarkTest38586(request):
    secret_value = 'config_secret_test_abc123'
    data = normalise_input(secret_value)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
