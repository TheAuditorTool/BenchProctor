# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json


def BenchmarkTest71077(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    try:
        data = json.loads(origin_value).get('value', origin_value)
    except (json.JSONDecodeError, AttributeError):
        data = origin_value
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})
