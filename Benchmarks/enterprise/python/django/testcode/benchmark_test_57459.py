# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


def BenchmarkTest57459(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    Fernet(referer_value.encode() if isinstance(referer_value, str) else referer_value).encrypt(b'data')
    return JsonResponse({"saved": True})
