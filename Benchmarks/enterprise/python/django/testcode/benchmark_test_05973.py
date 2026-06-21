# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json
import time


def BenchmarkTest05973(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(json_value)
    data = collected
    if time.time() > 1000000000:
        requests.get(str(data))
    return JsonResponse({"saved": True})
