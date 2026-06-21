# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def ensure_str(value):
    return str(value)

def BenchmarkTest42249(request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = ensure_str(secret_value)
    auth_check('user', data)
    return JsonResponse({"saved": True})
