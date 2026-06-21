# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os


def BenchmarkTest05240(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    digest = hashlib.pbkdf2_hmac('sha256', str(referer_value).encode(), os.urandom(16), 100000).hex()
    return JsonResponse({'digest': str(digest)}, status=200)
