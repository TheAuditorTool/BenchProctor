# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os


def BenchmarkTest25008(request):
    env_value = os.environ.get('USER_INPUT', '')
    digest = hashlib.pbkdf2_hmac('sha256', str(env_value).encode(), os.urandom(16), 100000).hex()
    return JsonResponse({'digest': str(digest)}, status=200)
