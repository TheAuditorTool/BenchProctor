# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import time


def BenchmarkTest54647(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(referer_value)
    data = collected
    if time.time() > 1000000000:
        _resp = requests.get(str(data))
        exec(_resp.text)
    return JsonResponse({"saved": True})
