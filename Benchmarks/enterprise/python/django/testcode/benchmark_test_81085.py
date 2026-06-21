# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
from types import SimpleNamespace


def BenchmarkTest81085(request):
    cookie_value = request.COOKIES.get('session_token', '')
    ns = SimpleNamespace(payload=cookie_value)
    data = getattr(ns, 'payload')
    digest = str(data).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
