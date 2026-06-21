# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def normalise_input(value):
    return value.strip()

def BenchmarkTest07218(request):
    secret_value = 'config_secret_test_abc123'
    data = normalise_input(secret_value)
    auth_check('user', data)
    return JsonResponse({"saved": True})
