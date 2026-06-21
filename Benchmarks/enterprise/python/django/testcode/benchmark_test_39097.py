# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os


def coalesce_blank(value):
    return value or ''

def BenchmarkTest39097(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = coalesce_blank(forwarded_ip)
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JsonResponse({'digest': str(digest)}, status=200)
