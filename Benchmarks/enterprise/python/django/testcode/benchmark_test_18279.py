# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import jwt


def BenchmarkTest18279(request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    data = f'{secret_value:.200s}'
    jwt.encode({'sub': 'user'}, data, algorithm='HS256')
    return JsonResponse({"saved": True})
