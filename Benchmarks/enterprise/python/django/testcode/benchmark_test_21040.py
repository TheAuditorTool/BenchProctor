# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest21040(request):
    host_value = request.META.get('HTTP_HOST', '')
    globals().setdefault('_secret_cache', {})['current'] = str(host_value)
    return JsonResponse({"saved": True})
