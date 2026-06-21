# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


def BenchmarkTest52448(request):
    host_value = request.META.get('HTTP_HOST', '')
    if host_value:
        data = host_value
    else:
        data = ''
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
