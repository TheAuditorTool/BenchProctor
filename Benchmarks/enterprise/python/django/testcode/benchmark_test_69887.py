# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest69887(request):
    secret_value = 'config_secret_test_abc123'
    auth_check('user', secret_value)
    return JsonResponse({"saved": True})
