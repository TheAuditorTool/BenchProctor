# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
from types import SimpleNamespace


def BenchmarkTest02982(request):
    xml_value = request.body.decode('utf-8')
    ns = SimpleNamespace(payload=xml_value)
    data = getattr(ns, 'payload')
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
