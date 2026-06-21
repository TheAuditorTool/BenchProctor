# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from types import SimpleNamespace
from app_runtime import auth_check


def BenchmarkTest26554(request, path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    if auth_check('user', str(data)):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
