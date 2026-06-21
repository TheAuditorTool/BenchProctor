# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


def BenchmarkTest60446(request):
    host_value = request.META.get('HTTP_HOST', '')
    Fernet(host_value.encode() if isinstance(host_value, str) else host_value).encrypt(b'data')
    return JsonResponse({"saved": True})
