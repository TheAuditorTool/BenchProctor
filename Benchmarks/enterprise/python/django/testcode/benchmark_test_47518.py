# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os


def BenchmarkTest47518(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    digest = hashlib.pbkdf2_hmac('sha256', str(auth_header).encode(), os.urandom(16), 100000).hex()
    return JsonResponse({'digest': str(digest)}, status=200)
