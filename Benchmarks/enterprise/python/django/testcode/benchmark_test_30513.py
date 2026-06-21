# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from cryptography.fernet import Fernet


def BenchmarkTest30513(request):
    cookie_value = request.COOKIES.get('session_token', '')
    Fernet(cookie_value.encode() if isinstance(cookie_value, str) else cookie_value).encrypt(b'data')
    return JsonResponse({"saved": True})
