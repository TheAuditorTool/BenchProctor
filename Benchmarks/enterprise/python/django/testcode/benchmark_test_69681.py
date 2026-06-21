# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
from types import SimpleNamespace


def BenchmarkTest69681(request):
    cookie_value = request.COOKIES.get('session_token', '')
    ns = SimpleNamespace(payload=cookie_value)
    data = getattr(ns, 'payload')
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
