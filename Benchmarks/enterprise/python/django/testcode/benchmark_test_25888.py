# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest25888(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    parts = []
    for token in str(referer_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    os.remove(str(data))
    return JsonResponse({"saved": True})
