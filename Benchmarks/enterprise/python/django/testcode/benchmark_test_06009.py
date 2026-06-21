# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os


def ensure_str(value):
    return str(value)

def BenchmarkTest06009(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = ensure_str(ua_value)
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JsonResponse({'digest': str(digest)}, status=200)
