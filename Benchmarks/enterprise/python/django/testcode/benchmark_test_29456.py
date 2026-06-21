# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


def BenchmarkTest29456(request):
    secret_value = ['s3cr3t_key_test_xyz'][0]
    Fernet(secret_value.encode() if isinstance(secret_value, str) else secret_value).encrypt(b'data')
    return JsonResponse({"saved": True})
