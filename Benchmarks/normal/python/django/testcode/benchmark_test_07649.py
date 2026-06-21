# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest07649(request):
    raw_body = request.body.decode('utf-8')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(raw_body)
    data = collected
    auth_check('user', data)
    return JsonResponse({"saved": True})
