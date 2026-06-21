# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest19606(request):
    secret_value = ['s3cr3t_key_test_xyz'][0]
    data = (lambda v: v.strip())(secret_value)
    auth_check('user', data)
    return JsonResponse({"saved": True})
