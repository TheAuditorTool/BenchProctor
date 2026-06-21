# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest41543(request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    auth_check('user', secret_value)
    return JsonResponse({"saved": True})
