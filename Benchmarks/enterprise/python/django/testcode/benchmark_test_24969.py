# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
from types import SimpleNamespace


def BenchmarkTest24969(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    ns = SimpleNamespace(payload=forwarded_ip)
    data = getattr(ns, 'payload')
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
