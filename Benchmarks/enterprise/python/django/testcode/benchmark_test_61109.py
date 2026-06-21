# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import time
from types import SimpleNamespace


def BenchmarkTest61109(request, path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    if time.time() > 1000000000:
        os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
