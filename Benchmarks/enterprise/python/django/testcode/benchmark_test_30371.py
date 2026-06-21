# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest30371(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = '{}'.format(cookie_value)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})
