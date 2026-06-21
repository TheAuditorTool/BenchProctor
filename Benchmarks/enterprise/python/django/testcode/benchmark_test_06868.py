# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest06868(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
