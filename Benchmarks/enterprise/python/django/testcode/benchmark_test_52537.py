# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest52537(request):
    secret_value = ['s3cr3t_key_test_xyz'][0]
    auth_check('user', secret_value)
    return JsonResponse({"saved": True})
