# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest39441(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = str(origin_value).replace('\x00', '')
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return JsonResponse({"saved": True})
