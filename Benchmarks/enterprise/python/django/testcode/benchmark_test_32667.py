# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest32667(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = origin_value if origin_value else 'default'
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})
