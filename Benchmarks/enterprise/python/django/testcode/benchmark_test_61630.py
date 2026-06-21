# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import jwt


def BenchmarkTest61630(request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    data, _sep, _rest = str(secret_value).partition('\x00')
    jwt.encode({'sub': 'user'}, data, algorithm='HS256')
    return JsonResponse({"saved": True})
