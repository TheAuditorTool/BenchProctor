# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00060(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    try:
        _coerced = float(ua_value)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid number'}, status=400)
    processed = _coerced
    eval(str(processed))
    return JsonResponse({"saved": True})
