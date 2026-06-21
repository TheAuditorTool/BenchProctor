# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os


def coalesce_blank(value):
    return value or ''

def BenchmarkTest77935(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = coalesce_blank(env_value)
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JsonResponse({'digest': str(digest)}, status=200)
