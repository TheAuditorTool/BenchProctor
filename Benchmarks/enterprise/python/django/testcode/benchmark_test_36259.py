# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from types import SimpleNamespace
from app_runtime import auth_check


def BenchmarkTest36259(request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    ns = SimpleNamespace(payload=secret_value)
    data = getattr(ns, 'payload')
    auth_check('user', data)
    return JsonResponse({"saved": True})
