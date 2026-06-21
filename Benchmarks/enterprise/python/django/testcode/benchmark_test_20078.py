# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest20078(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    _resp = requests.get(str(origin_value))
    exec(_resp.text)
    return JsonResponse({"saved": True})
