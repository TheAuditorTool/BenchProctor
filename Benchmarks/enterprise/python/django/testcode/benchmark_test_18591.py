# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest18591(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = f'{cookie_value}'
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
