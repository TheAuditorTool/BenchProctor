# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from types import SimpleNamespace
from app_runtime import auth_check


def BenchmarkTest11189(request):
    user_id = request.GET.get('id', '')
    ns = SimpleNamespace(payload=user_id)
    data = getattr(ns, 'payload')
    auth_check('user', data)
    return JsonResponse({"saved": True})
