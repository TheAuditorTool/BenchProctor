# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest09865(request):
    cookie_value = request.COOKIES.get('session_token', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(cookie_value)
    data = collected
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
