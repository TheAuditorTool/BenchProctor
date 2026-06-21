# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


def BenchmarkTest36599(request):
    secret_value = ['s3cr3t_key_test_xyz'][0]
    data = secret_value if secret_value else 'default'
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
