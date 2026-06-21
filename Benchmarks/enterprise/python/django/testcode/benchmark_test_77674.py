# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest77674(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    def normalize(value):
        return value.strip()
    data = normalize(origin_value)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return JsonResponse({"saved": True})
