# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest57834(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    _resp = requests.get(str(referer_value))
    exec(_resp.text)
    return JsonResponse({"saved": True})
