# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def normalise_input(value):
    return value.strip()

def BenchmarkTest14082(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = normalise_input(cookie_value)
    json.loads(data)
    return JsonResponse({"saved": True})
