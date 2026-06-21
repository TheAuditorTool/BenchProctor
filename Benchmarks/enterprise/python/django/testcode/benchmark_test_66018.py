# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest66018(request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = (lambda v: v.strip())(secret_value)
    auth_check('user', data)
    return JsonResponse({"saved": True})
