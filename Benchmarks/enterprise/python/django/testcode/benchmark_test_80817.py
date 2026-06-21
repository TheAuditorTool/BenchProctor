# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from types import SimpleNamespace


def BenchmarkTest80817(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    ns = SimpleNamespace(payload=auth_header)
    data = getattr(ns, 'payload')
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
