# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest18314(request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    def normalize(value):
        return value.strip()
    data = normalize(secret_value)
    auth_check('user', data)
    return JsonResponse({"saved": True})
