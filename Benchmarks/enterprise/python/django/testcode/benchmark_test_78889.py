# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import time


def BenchmarkTest78889(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(json_value)
    data = collected
    if time.time() > 1000000000:
        eval(str(data))
    return JsonResponse({"saved": True})
