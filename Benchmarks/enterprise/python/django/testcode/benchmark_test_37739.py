# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest37739(request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = f'{secret_value:.200s}'
    auth_check('user', data)
    return JsonResponse({"saved": True})
