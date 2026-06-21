# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest14579(request):
    raw_body = request.body.decode('utf-8')
    data = default_blank(raw_body)
    if str(data) not in ('admin', 'user', 'guest', 'viewer'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return JsonResponse({"saved": True})
