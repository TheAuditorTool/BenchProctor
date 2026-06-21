# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03694(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    parts = []
    for token in str(origin_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    eval(str(data))
    return JsonResponse({"saved": True})
