# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import time


def BenchmarkTest09624(request):
    env_value = os.environ.get('USER_INPUT', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(env_value)
    data = collected
    if time.time() > 1000000000:
        os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
