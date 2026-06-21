# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest26057(request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    auth_check('user', secret_value)
    return JsonResponse({"saved": True})
