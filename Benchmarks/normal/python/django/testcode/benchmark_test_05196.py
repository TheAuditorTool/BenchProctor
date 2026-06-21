# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest05196(request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    parts = str(secret_value).split(',')
    data = ','.join(parts)
    auth_check('user', data)
    return JsonResponse({"saved": True})
