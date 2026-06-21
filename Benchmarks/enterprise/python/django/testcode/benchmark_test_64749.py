# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest64749(request):
    cookie_value = request.COOKIES.get('session_token', '')
    parts = str(cookie_value).split(',')
    data = ','.join(parts)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})
