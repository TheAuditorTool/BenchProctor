# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import unquote


def BenchmarkTest32422(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = unquote(cookie_value)
    requests.get(str(data))
    return JsonResponse({"saved": True})
