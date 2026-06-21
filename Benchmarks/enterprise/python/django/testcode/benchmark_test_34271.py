# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest34271(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = ' '.join(str(cookie_value).split())
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})
