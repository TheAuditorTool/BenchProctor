# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest74072(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    prefix = ''
    data = prefix + str(referer_value)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return JsonResponse({"saved": True})
