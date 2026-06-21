# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def relay_value(value):
    return value

def BenchmarkTest23854(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = relay_value(origin_value)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return JsonResponse({"saved": True})
