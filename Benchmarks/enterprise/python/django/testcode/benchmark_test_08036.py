# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest08036(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = ' '.join(str(referer_value).split())
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return JsonResponse({"saved": True})
