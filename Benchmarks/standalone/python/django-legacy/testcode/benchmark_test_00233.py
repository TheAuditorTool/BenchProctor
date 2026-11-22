# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.core.cache import cache


def BenchmarkTest00233(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    cache.set('active_tenant', str(header_value), None)
    return JsonResponse({"saved": True})
