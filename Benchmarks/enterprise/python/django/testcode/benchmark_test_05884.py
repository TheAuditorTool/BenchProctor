# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import json
from types import SimpleNamespace


def BenchmarkTest05884(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    ns = SimpleNamespace(payload=json_value)
    data = getattr(ns, 'payload')
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
