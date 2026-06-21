# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os


def BenchmarkTest80505(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    digest = hashlib.pbkdf2_hmac('sha256', str(header_value).encode(), os.urandom(16), 100000).hex()
    return JsonResponse({'digest': str(digest)}, status=200)
