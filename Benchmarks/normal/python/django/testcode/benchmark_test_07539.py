# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest07539(request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = str(secret_value).replace('\x00', '')
    auth_check('user', data)
    return JsonResponse({"saved": True})
