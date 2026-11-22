# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.core.cache import cache
import re


def BenchmarkTest00039(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    def normalize(value):
        return value.strip()
    data = normalize(referer_value)
    if not re.fullmatch("^[a-zA-Z0-9 _.\\-]+$", data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    cache.set('active_tenant', str(processed), None)
    return JsonResponse({"saved": True})
