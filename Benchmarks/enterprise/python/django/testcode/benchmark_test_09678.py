# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json


def BenchmarkTest09678(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    try:
        data = json.loads(auth_header).get('value', auth_header)
    except (json.JSONDecodeError, AttributeError):
        data = auth_header
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
