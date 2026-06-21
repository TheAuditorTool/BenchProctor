# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


def BenchmarkTest23429(request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    if secret_value:
        data = secret_value
    else:
        data = ''
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
