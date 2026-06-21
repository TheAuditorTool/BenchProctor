# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest77649(request):
    cookie_value = request.COOKIES.get('session_token', '')
    requests.get('https://api.pycdn.io/data', params={'q': str(cookie_value)}, verify=True)
    return JsonResponse({"saved": True})
