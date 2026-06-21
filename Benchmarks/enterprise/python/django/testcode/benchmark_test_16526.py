# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os
from types import SimpleNamespace


def BenchmarkTest16526(request):
    env_value = os.environ.get('USER_INPUT', '')
    ns = SimpleNamespace(payload=env_value)
    data = getattr(ns, 'payload')
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})
