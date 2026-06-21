# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest20527(request):
    host_value = request.META.get('HTTP_HOST', '')
    if host_value:
        data = host_value
    else:
        data = ''
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return JsonResponse({"saved": True})
