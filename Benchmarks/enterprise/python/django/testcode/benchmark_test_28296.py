# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import time


def BenchmarkTest28296(request, path_param):
    path_value = path_param
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(path_value)
    data = collected
    if time.time() > 1000000000:
        with open('/var/log/app_audit.log', 'a') as fh:
            fh.write(str(data))
    return JsonResponse({"saved": True})
