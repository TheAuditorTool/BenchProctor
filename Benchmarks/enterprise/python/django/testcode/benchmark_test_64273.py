# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import jwt


def BenchmarkTest64273(request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    if secret_value:
        data = secret_value
    else:
        data = ''
    jwt.encode({'sub': 'user'}, data, algorithm='HS256')
    return JsonResponse({"saved": True})
