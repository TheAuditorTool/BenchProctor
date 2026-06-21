# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import base64


def BenchmarkTest59450(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})
