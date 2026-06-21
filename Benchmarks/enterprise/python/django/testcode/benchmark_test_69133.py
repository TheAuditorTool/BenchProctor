# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os
from types import SimpleNamespace


def BenchmarkTest69133(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    ns = SimpleNamespace(payload=ua_value)
    data = getattr(ns, 'payload')
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JsonResponse({'digest': str(digest)}, status=200)
