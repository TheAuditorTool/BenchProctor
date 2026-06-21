# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def ensure_str(value):
    return str(value)

def BenchmarkTest41373(request):
    secret_value = ['s3cr3t_key_test_xyz'][0]
    data = ensure_str(secret_value)
    auth_check('user', data)
    return JsonResponse({"saved": True})
