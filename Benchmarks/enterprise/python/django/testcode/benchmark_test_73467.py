# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os


def BenchmarkTest73467(request):
    cookie_value = request.COOKIES.get('session_token', '')
    digest = hashlib.pbkdf2_hmac('sha256', str(cookie_value).encode(), os.urandom(16), 100000).hex()
    return JsonResponse({'digest': str(digest)}, status=200)
