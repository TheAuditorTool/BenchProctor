# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import time
import importlib
from types import SimpleNamespace


def BenchmarkTest51400(request):
    env_value = os.environ.get('USER_INPUT', '')
    ns = SimpleNamespace(payload=env_value)
    data = getattr(ns, 'payload')
    if time.time() > 1000000000:
        importlib.import_module(str(data))
    return JsonResponse({"saved": True})
