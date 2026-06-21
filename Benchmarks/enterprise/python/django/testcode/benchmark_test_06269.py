# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest06269(request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = default_blank(secret_value)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
