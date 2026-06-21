# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest43736(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    if origin_value:
        data = origin_value
    else:
        data = ''
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})
