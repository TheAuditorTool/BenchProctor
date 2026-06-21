# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


def BenchmarkTest40248(request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    Fernet(secret_value.encode() if isinstance(secret_value, str) else secret_value).encrypt(b'data')
    return JsonResponse({"saved": True})
