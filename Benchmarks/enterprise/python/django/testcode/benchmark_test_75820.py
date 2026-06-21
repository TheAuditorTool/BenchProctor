# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest75820(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    parts = []
    for token in str(origin_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})
