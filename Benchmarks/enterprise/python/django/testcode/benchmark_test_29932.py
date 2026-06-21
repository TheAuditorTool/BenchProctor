# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from types import SimpleNamespace


def BenchmarkTest29932(request):
    raw_body = request.body.decode('utf-8')
    ns = SimpleNamespace(payload=raw_body)
    data = getattr(ns, 'payload')
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})
