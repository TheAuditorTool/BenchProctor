# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest70763(request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = default_blank(secret_value)
    auth_check('user', data)
    return JsonResponse({"saved": True})
