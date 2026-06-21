# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def BenchmarkTest25646(request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    data = '%s' % (secret_value,)
    auth_check('user', data)
    return JsonResponse({"saved": True})
