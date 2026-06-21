# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest64362(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    parts = []
    for token in str(origin_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
