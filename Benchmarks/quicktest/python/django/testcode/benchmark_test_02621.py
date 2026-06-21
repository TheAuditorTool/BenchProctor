# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02621(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = (lambda v: v.strip())(ua_value)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return JsonResponse({"saved": True})
