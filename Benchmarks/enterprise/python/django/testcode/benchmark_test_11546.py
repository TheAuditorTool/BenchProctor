# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os


def BenchmarkTest11546(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    digest = hashlib.pbkdf2_hmac('sha256', str(origin_value).encode(), os.urandom(16), 100000).hex()
    return JsonResponse({'digest': str(digest)}, status=200)
