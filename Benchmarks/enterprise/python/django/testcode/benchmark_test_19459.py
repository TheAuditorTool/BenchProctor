# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os


def coalesce_blank(value):
    return value or ''

def BenchmarkTest19459(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = coalesce_blank(origin_value)
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JsonResponse({'digest': str(digest)}, status=200)
