# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest45715(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    parts = []
    for token in str(origin_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    try:
        int(str(data))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
