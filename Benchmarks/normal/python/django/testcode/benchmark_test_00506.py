# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from types import SimpleNamespace


def BenchmarkTest00506(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    ns = SimpleNamespace(payload=ua_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(processed)})
