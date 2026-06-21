# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest17701(request):
    secret_value = ['s3cr3t_key_test_xyz'][0]
    data = ' '.join(str(secret_value).split())
    auth_check('user', data)
    return JsonResponse({"saved": True})
