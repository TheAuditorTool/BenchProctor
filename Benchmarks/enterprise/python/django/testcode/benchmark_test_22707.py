# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from types import SimpleNamespace


def BenchmarkTest22707(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    ns = SimpleNamespace(payload=auth_header)
    data = getattr(ns, 'payload')
    eval(compile('eval(str(data))', '<sink>', 'exec'))
    return JsonResponse({"saved": True})
