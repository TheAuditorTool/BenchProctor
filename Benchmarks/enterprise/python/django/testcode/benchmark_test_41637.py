# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest41637(request):
    secret_value = 'config_secret_test_abc123'
    data = secret_value if secret_value else 'default'
    auth_check('user', data)
    return JsonResponse({"saved": True})
