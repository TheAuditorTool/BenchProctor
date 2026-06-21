# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest78181(request):
    secret_value = 'config_secret_test_abc123'
    data = str(secret_value).replace('\x00', '')
    auth_check('user', data)
    return JsonResponse({"saved": True})
