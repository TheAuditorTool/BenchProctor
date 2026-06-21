# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest04454(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data, _sep, _rest = str(ua_value).partition('\x00')
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return JsonResponse({"saved": True})
