# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def relay_value(value):
    return value

def BenchmarkTest49960(request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    data = relay_value(secret_value)
    processed = data[:64]
    auth_check('user', processed)
    return JsonResponse({"saved": True})
