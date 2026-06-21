# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest08420(request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    data = (lambda v: v.strip())(secret_value)
    auth_check('user', data)
    return JsonResponse({"saved": True})
