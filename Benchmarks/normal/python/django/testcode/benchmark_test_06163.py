# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest06163(request):
    cookie_value = request.COOKIES.get('session_token', '')
    requests.post('http://api.prod.internal/data', data=str(cookie_value))
    return JsonResponse({"saved": True})
