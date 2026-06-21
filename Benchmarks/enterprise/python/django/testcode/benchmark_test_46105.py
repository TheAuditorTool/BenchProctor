# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import unquote


def BenchmarkTest46105(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = unquote(cookie_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})
