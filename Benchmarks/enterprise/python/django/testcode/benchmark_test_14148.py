# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import time


def BenchmarkTest14148(request):
    host_value = request.META.get('HTTP_HOST', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(host_value)
    data = collected
    if time.time() > 1000000000:
        requests.get(str(data))
    return JsonResponse({"saved": True})
