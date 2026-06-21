# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os


def to_text(value):
    return str(value).strip()

def BenchmarkTest81146(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = to_text(header_value)
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JsonResponse({'digest': str(digest)}, status=200)
