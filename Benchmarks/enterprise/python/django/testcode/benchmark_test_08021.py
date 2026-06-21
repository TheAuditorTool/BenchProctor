# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest08021(request):
    cookie_value = request.COOKIES.get('session_token', '')
    requests.post('https://api.prod.internal/data', data=str(cookie_value), verify=True)
    return JsonResponse({"saved": True})
