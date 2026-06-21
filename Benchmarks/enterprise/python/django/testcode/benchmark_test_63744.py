# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest63744(request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    parts = str(secret_value).split(',')
    data = ','.join(parts)
    auth_check('user', data)
    return JsonResponse({"saved": True})
