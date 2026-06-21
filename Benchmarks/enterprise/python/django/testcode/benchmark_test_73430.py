# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from types import SimpleNamespace
from app_runtime import auth_check


def BenchmarkTest73430(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    ns = SimpleNamespace(payload=config_value)
    data = getattr(ns, 'payload')
    auth_check('user', data)
    return JsonResponse({"saved": True})
