# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest67761(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    parts = []
    for token in str(referer_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    eval(str(data))
    return JsonResponse({"saved": True})
