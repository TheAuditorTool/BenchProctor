# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest23377(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = '{}'.format(origin_value)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return JsonResponse({"saved": True})
