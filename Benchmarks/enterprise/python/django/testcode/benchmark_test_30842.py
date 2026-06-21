# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def to_text(value):
    return str(value).strip()

def BenchmarkTest30842(request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    data = to_text(secret_value)
    auth_check('user', data)
    return JsonResponse({"saved": True})
