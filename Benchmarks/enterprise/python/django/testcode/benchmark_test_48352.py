# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest48352(request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    data = f'{secret_value:.200s}'
    auth_check('user', data)
    return JsonResponse({"saved": True})
