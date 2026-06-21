# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest06093(request):
    secret_value = 'config_secret_test_abc123'
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(secret_value)
    data = collected
    auth_check('user', data)
    return JsonResponse({"saved": True})
