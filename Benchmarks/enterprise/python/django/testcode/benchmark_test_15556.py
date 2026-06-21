# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
from types import SimpleNamespace


def BenchmarkTest15556(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    ns = SimpleNamespace(payload=origin_value)
    data = getattr(ns, 'payload')
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
