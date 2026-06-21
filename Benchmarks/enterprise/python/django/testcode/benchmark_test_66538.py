# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from types import SimpleNamespace


def BenchmarkTest66538(request):
    xml_value = request.body.decode('utf-8')
    ns = SimpleNamespace(payload=xml_value)
    data = getattr(ns, 'payload')
    if str(data) in ('admin', 'true', 'authenticated'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
