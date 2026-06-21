# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from types import SimpleNamespace


def BenchmarkTest12489(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    ns = SimpleNamespace(payload=origin_value)
    data = getattr(ns, 'payload')
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
