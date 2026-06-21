# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import time
from types import SimpleNamespace


def BenchmarkTest63860(request, path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    if time.time() > 1000000000:
        exec(str(data))
    return JsonResponse({"saved": True})
