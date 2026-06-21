# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest61503(request):
    user_id = request.GET.get('id', '')
    ctx = RequestContext(user_id)
    data = ctx.payload
    if str(data).lower() not in ('true', 'false'):
        return JsonResponse({'error': 'invalid boolean'}, status=400)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return JsonResponse({"saved": True})
