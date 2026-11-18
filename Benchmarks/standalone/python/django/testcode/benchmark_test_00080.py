# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00080(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = (lambda v: v.strip())(auth_header)
    try:
        _coerced = float(data)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid number'}, status=400)
    processed = _coerced
    exec(str(processed))
    return JsonResponse({"saved": True})
