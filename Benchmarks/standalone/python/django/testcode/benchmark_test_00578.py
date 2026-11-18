# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00578(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    parts = []
    for token in str(origin_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    exec(str(data))
    return JsonResponse({"saved": True})
