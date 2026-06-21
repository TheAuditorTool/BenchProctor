# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


def BenchmarkTest05378(request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    prefix = ''
    data = prefix + str(secret_value)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
