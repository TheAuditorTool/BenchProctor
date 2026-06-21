# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def ensure_str(value):
    return str(value)

def BenchmarkTest31719(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = ensure_str(cookie_value)
    digest = hashlib.sha256(('static_salt_123' + str(data)).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
