# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from types import SimpleNamespace


def BenchmarkTest27789(request, path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    if str(data) in ('localhost', 'internal-gateway'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
