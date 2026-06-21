# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import time


def BenchmarkTest61405(request):
    user_id = request.GET.get('id', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(user_id)
    data = collected
    if time.time() > 1000000000:
        eval(str(data))
    return JsonResponse({"saved": True})
