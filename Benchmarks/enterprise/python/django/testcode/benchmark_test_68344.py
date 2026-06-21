# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
from types import SimpleNamespace


def BenchmarkTest68344(request):
    raw_body = request.body.decode('utf-8')
    ns = SimpleNamespace(payload=raw_body)
    data = getattr(ns, 'payload')
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
