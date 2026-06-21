# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


def BenchmarkTest46082(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    def normalize(value):
        return value.strip()
    data = normalize(auth_header)
    Fernet(data.encode() if isinstance(data, str) else data).encrypt(b'data')
    return JsonResponse({"saved": True})
