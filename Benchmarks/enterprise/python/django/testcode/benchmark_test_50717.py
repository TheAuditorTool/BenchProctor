# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest50717(request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    data = default_blank(secret_value)
    auth_check('user', data)
    return JsonResponse({"saved": True})
