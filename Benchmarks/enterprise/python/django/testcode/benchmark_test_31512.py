# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


def BenchmarkTest31512(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    Fernet(origin_value.encode() if isinstance(origin_value, str) else origin_value).encrypt(b'data')
    return JsonResponse({"saved": True})
