# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.core.cache import cache


def BenchmarkTest00014(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = f'{forwarded_ip!s}'
    try:
        _coerced = float(data)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid number'}, status=400)
    processed = _coerced
    cache.set('active_tenant', str(processed), None)
    return JsonResponse({"saved": True})
