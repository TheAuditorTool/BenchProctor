# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest11043(request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    if secret_value:
        data = secret_value
    else:
        data = ''
    auth_check('user', data)
    return JsonResponse({"saved": True})
