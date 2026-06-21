# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os


def BenchmarkTest78229(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    digest = hashlib.pbkdf2_hmac('sha256', str(ua_value).encode(), os.urandom(16), 100000).hex()
    return JsonResponse({'digest': str(digest)}, status=200)
