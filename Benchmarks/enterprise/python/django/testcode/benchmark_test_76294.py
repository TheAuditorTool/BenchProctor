# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest76294(request):
    cookie_value = request.COOKIES.get('session_token', '')
    requests.get(str(cookie_value))
    return JsonResponse({"saved": True})
