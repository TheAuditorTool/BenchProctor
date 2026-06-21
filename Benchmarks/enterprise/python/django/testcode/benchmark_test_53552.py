# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest53552(request):
    secret_value = 'config_secret_test_abc123'
    data = f'{secret_value}'
    auth_check('user', data)
    return JsonResponse({"saved": True})
