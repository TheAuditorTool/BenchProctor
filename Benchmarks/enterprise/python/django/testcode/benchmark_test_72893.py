# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


def BenchmarkTest72893(request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = ' '.join(str(secret_value).split())
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
