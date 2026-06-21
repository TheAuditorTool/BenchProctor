# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest57645(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    parts = []
    for token in str(forwarded_ip).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})
